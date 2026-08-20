from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario, ProfesorFormulario, EstudianteForm

def index(request):
    return render(request, 'myapp/index.html')

# --- ESTUDIANTES ---

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/estudiante_detail.html', {'estudiante': estudiante})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiante_form.html', {'form': form})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('myapp:estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'myapp/estudiante_form.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('myapp:estudiantes')
    return render(request, 'myapp/estudiante_confirm_delete.html', {'estudiante': estudiante})


# --- CURSOS ---

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos})

def cursoFormulario(request):
    if request.method == "POST":
        form = CursoFormulario(request.POST)
        if form.is_valid():
            Curso.objects.create(
                nombre=form.cleaned_data["nombre"],
                camada=form.cleaned_data["camada"]
            )
            return render(request, "myapp/curso_exito.html")
    else:
        form = CursoFormulario()
    return render(request, "myapp/curso_formulario.html", {"form": form})


# --- PROFESORES ---

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})

def profesorFormulario(request):
    if request.method == "POST":
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            Profesor.objects.create(
                nombre=form.cleaned_data["nombre"],
                apellido=form.cleaned_data["apellido"],
                email=form.cleaned_data["email"],
                profesion=form.cleaned_data["profesion"],
                materiaAsignada=form.cleaned_data["materiaAsignada"]
            )
            return render(request, "myapp/profesor_exito.html")
    else:
        form = ProfesorFormulario()
    return render(request, "myapp/profesor_formulario.html", {"form": form})


# --- ENTREGABLES ---

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html', {'entregables': entregables})