from django import forms
from .models import Ciudad
from pais.models import Pais

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['pais', 'codigo', 'descripcion', 'isActive']
        widgets = {
            'pais': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width: 100%'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: BUE'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Buenos Aires'
            }),
            'isActive': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'pais': 'País',
            'codigo': 'Código de ciudad',
            'descripcion': 'Nombre de la ciudad',
            'isActive': '¿Activa?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pais'].queryset = Pais.objects.filter(isActive=True, deleted=False)