from django import forms
from .models import Estudiante, Curso, Profesor

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'imagen', 'activo', 'fecha_fin']
        widgets = {
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion', 'curso_asignado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'Ej: Ana'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'Ej: Pérez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg rounded-3 fs-6 custom-input', 'placeholder': 'ejemplo@correo.com'}),
            'profesion': forms.Select(attrs={'class': 'form-select form-select-lg rounded-3 fs-6 custom-input'}),
            'curso_asignado': forms.Select(attrs={'class': 'form-select form-select-lg rounded-3 fs-6 custom-input'}),
        }