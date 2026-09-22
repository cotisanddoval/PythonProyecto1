from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_guardar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        # Asegura que si el perfil ya existe, guarde los cambios
        if hasattr(instance, 'perfil'):
            instance.perfil.save()