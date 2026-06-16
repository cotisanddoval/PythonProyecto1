from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación Django"}
    return render(request, "myapp/index.html", context)
