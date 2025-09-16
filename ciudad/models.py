from django.db import models
from pais.models import Pais
from django.core.exceptions import ValidationError

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, verbose_name='País')
    codigo = models.CharField(max_length=10, verbose_name='Código')
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    isActive = models.BooleanField(default=True, verbose_name='¿Activo?')
    deleted = models.BooleanField(default=False, verbose_name='¿Eliminado?')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['descripcion']
        unique_together = ['pais', 'codigo']

    def __str__(self):
        return f"{self.descripcion} ({self.pais.codigo})"
    
    def clean(self):
        """Valida la unicidad antes de guardar"""
        if not self.deleted:
            if Ciudad.objects.filter(
                pais=self.pais, 
                codigo=self.codigo,
                deleted=False
            ).exclude(pk=self.pk).exists():
                raise ValidationError(
                    f"Ya existe una ciudad activa con el código {self.codigo} "
                    f"para el país {self.pais}"
                )

    def delete(self, *args, **kwargs):
        """Borrado lógico"""
        self.deleted = True
        self.isActive = False
        self.save()

    def restore(self):
        """Restaurar ciudad eliminada"""
        self.deleted = False
        self.save()