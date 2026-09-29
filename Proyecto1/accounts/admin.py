from django.contrib import admin
from .models import Perfil

# Registramos el modelo Perfil para poder editarlo desde el panel
admin.site.register(Perfil)