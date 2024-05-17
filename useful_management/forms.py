# useful_management/forms.py
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['usuario', 'nombre_completo', 'motivo', 'mensaje']  # Incluye 'usuario'
        widgets = {
            'usuario': forms.HiddenInput(),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user is not None:
            self.fields['usuario'].initial = self.user