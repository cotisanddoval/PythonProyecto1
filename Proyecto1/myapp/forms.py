from django import forms
from django.contrib.auth.models import User
from .models import Estudiante, Profesor, Curso, TrabajoPractico, Entrega

class EstudianteForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 custom-input'}), required=True, label="Contraseña inicial")

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'username', 'password']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3 custom-input'}),
        }
        
class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'imagen', 'activo', 'fecha_inicio', 'fecha_fin', 'password_curso']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg rounded-3 custom-input'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg rounded-3 custom-input'}),
        }

class ProfesorForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de Usuario", required=True, widget=forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 custom-input'}), required=True, label="Contraseña inicial")

    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion', 'curso_asignado', 'username', 'password']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'Ej: Ana'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'Ej: Pérez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'ejemplo@correo.com'}),
            'profesion': forms.Select(attrs={'class': 'form-select form-select-lg rounded-3 fs-6 custom-input'}),
            'curso_asignado': forms.Select(attrs={'class': 'form-select form-select-lg rounded-3 fs-6 custom-input'}),
        }
        
class TrabajoPracticoForm(forms.ModelForm):
    class Meta:
        model = TrabajoPractico
        fields = ['titulo', 'descripcion', 'curso', 'fecha_entrega']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control rounded-3 custom-input', 'rows': 3}),
            'curso': forms.Select(attrs={'class': 'form-select rounded-3 custom-input'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control rounded-3 custom-input', 'type': 'date'}),
        }

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        # Solo permitimos que el alumno suba el archivo. La nota queda excluida.
        fields = ['archivo'] 
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3 custom-input'}),
        }