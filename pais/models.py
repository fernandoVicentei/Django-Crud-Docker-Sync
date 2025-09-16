from django.db import models

class Pais(models.Model):
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.isActive = False
        self.save()
    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"