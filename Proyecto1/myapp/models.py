# Create your models here.

from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    
    # Nuevos campos:
    activo = models.BooleanField(default=True, verbose_name="¿Curso Activo?")
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de Finalización")
    # En tu models.py, dentro de la clase Curso:
    password_curso = models.CharField(max_length=50, blank=True, null=True, verbose_name="Contraseña del curso")

    def __str__(self):
        return f"{self.nombre} (Camada {self.camada})"

class Profesor(models.Model):
    ROLES = [
        ('Profesor', 'Profesor'),
        ('Profesora', 'Profesora'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=20, choices=ROLES, default='Profesor', verbose_name="Título / Rol")
    curso_asignado = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Curso Asignado")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class TrabajoPractico(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Trabajo Práctico")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Consigna / Descripción")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='trabajos_practicos', verbose_name="Curso")
    fecha_entrega = models.DateField(verbose_name="Fecha Límite de Entrega")

    def __str__(self):
        return f"{self.titulo} - {self.curso.nombre}"


class Entrega(models.Model):
    trabajo_practico = models.ForeignKey(TrabajoPractico, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='entregas')
    
    # El alumno sube su archivo aquí
    archivo = models.FileField(upload_to='entregas_archivos/', null=True, blank=True, verbose_name="Archivo Adjunto")
    
    fecha_subida = models.DateTimeField(auto_now=True)
    entregado = models.BooleanField(default=False, verbose_name="¿Entregado?")
    nota = models.FloatField(null=True, blank=True, verbose_name="Calificación")

    def __str__(self):
        return f"Entrega de {self.estudiante.nombre} - {self.trabajo_practico.titulo}"