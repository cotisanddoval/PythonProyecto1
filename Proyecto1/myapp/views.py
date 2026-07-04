from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario

def index(request):
    return render(request, 'myapp/index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/estudiante_detail.html', {'estudiante': estudiante})


# NUEVAS VISTAS

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html', {'entregables': entregables})

def cursoFormulario(request):
    if request.method == "POST":
        form = CursoFormulario(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            camada = form.cleaned_data["camada"]

            curso = Curso(nombre=nombre, camada=camada)
            curso.save()

            return render(request, "myapp/curso_exito.html")

    else:
        form = CursoFormulario()

    return render(request, "myapp/curso_formulario.html", {"form": form})