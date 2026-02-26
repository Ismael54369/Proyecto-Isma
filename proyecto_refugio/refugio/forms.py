from django import forms
from .models import SolicitudAdopcion, Donacion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['telefono', 'tipo_vivienda', 'experiencia_previa', 'otras_mascotas', 'horas_solitario', 'motivo']
        labels = {
            'telefono': 'Teléfono de contacto:',
            'tipo_vivienda': '¿Dónde vivirá el animal?',
            'experiencia_previa': '¿Has tenido animales de esta especie antes?',
            'otras_mascotas': '¿Conviven otras mascotas en casa actualmente?',
            'horas_solitario': 'Horas al día que el animal pasará solo en casa:',
            'motivo': 'Tu motivación para adoptar:',
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 600 123 456'}),
            'tipo_vivienda': forms.Select(attrs={'class': 'form-select'}),
            'experiencia_previa': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'}),
            'otras_mascotas': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'}),
            'horas_solitario': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 24}),
            'motivo': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Ej: Dispongo de tiempo libre, salgo a correr por las mañanas...'
            }),
        }

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['cantidad', 'mensaje']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control form-control-lg text-center fw-bold text-success', 'min': 1, 'step': 1, 'placeholder': 'Ej: 10'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ej: ¡Recupérate pronto, pequeño!'}),
        }