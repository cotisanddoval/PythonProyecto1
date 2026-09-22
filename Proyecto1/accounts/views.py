from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Cliente

# Ejemplo para Vistas Basadas en Funciones (FBV)
@login_required
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'myapp/clientes.html', {'clientes': clientes})

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    return render(request, 'myapp/eliminar_cliente.html', {'cliente': cliente})

# Ejemplo para Vistas Basadas en Clases (CBV)
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'myapp/clientes.html'
    context_object_name = 'clientes'