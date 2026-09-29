from django import forms
from .models import Estudiante, Curso, Profesor, Entregable

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'imagen', 'activo', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg rounded-3 custom-input'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg rounded-3 custom-input'}),
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
        
class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'curso', 'estudiante', 'fecha_inicio', 'entregado', 'nota']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control rounded-3 custom-input'}),
            'curso': forms.Select(attrs={'class': 'form-select rounded-3 custom-input'}),
            'estudiante': forms.Select(attrs={'class': 'form-select rounded-3 custom-input'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control rounded-3 custom-input', 'type': 'date'}),
            'entregado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control rounded-3 custom-input', 'step': '0.1'}),
        }