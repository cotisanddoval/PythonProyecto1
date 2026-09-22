from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Perfil

# Vistas Basadas en Funciones (FBV)

@login_required
def usuarios_list(request):
    perfiles = Perfil.objects.all()
    return render(request, 'accounts/usuarios.html', {'perfiles': perfiles})

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('accounts:usuarios')
    return render(request, 'accounts/eliminar_usuario.html', {'usuario': usuario})


# Vistas Basadas en Clases (CBV)

class PerfilListView(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'accounts/usuarios.html'
    context_object_name = 'perfiles'