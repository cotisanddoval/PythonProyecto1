from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Correo Electrónico")
    profesion = forms.CharField(max_length=100, label="Profesión")
    materiaAsignada = forms.CharField(max_length=100, label="Materia Asignada")