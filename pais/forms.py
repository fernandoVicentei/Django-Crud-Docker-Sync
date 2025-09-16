from django import forms
from .models import Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['codigo', 'descripcion', 'isActive']
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: BO'
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Bolivia'
            }),
            'isActive': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'codigo': 'Código del país',
            'descripcion': 'Nombre del país',
            'isActive': '¿Activo?'
        }