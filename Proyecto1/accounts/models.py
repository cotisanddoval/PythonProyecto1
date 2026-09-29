from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Definimos las opciones de roles
    OPCIONES_ROL = (
        ('admin', 'Administrador'),
        ('profesor', 'Profesor'),
        ('alumno', 'Alumno'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Nuevo campo para el rol (por defecto, los que se registran son alumnos)
    rol = models.CharField(max_length=20, choices=OPCIONES_ROL, default='alumno')

    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"