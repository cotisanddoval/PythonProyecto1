from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Usamos get_or_create para evitar el error de duplicidad si el perfil ya existe
            Perfil.objects.get_or_create(user=user)
            login(request, user)
            return redirect('myapp:index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('accounts:perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'accounts/perfil.html', {'form': form})