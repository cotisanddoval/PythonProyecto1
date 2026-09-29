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
    
    # Nuevos campos para manejar el estado y la fecha:
    activo = models.BooleanField(default=True, verbose_name="¿Curso Activo?")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de Finalización")

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

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre