from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    # Creamos las opciones para el registro (dejamos fuera al admin por seguridad)
    OPCIONES_REGISTRO = [
        ('alumno', 'Soy Alumno/a'),
        ('profesor', 'Soy Profesor/a'),
    ]
    rol = forms.ChoiceField(choices=OPCIONES_REGISTRO, required=True, initial='alumno')
    
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica el estilo a todos los campos
        for field_name, field in self.fields.items():
            if field_name == 'rol':
                field.widget.attrs.update({'class': 'form-select rounded-3 custom-input'})
            else:
                field.widget.attrs.update({'class': 'form-control rounded-3 custom-input'})

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'fecha_nacimiento']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3 custom-input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control rounded-3 custom-input', 'type': 'date'}),
        }