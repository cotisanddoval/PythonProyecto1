from django.contrib import admin
from .models import Curso, Profesor, Estudiante, TrabajoPractico, Entrega

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(TrabajoPractico)
admin.site.register(Entrega)