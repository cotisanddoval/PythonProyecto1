from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, TrabajoPractico, Entrega
from .forms import CursoFormulario, ProfesorForm, EstudianteForm, TrabajoPracticoForm, EntregaForm

def index(request):
    return render(request, 'myapp/index.html')

# --- ESTUDIANTES ---

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes.html', {'estudiantes': estudiantes})

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
    if request.method == 'POST':
        form = CursoFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:cursos')
    else:
        form = CursoFormulario()
       
    return render(request, 'myapp/curso_formulario.html', {'form': form})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoFormulario(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('myapp:cursos')
    else:
        form = CursoFormulario(instance=curso)
    
    return render(request, 'myapp/curso_formulario.html', {'form': form})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('myapp:cursos')
    return render(request, 'myapp/curso_confirm_delete.html', {'curso': curso})


# --- PROFESORES ---

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})

def profesorFormulario(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            Profesor.objects.create(
                nombre=form.cleaned_data["nombre"],
                apellido=form.cleaned_data["apellido"],
                email=form.cleaned_data["email"],
                profesion=form.cleaned_data["profesion"],
                curso_asignado=form.cleaned_data["curso_asignado"]
            )
            return render(request, "myapp/profesor_exito.html")
    else:
        form = ProfesorForm()
    return render(request, "myapp/profesor_formulario.html", {"form": form})

def editar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor.nombre = form.cleaned_data["nombre"]
            profesor.apellido = form.cleaned_data["apellido"]
            profesor.email = form.cleaned_data["email"]
            profesor.profesion = form.cleaned_data["profesion"]
            profesor.curso_asignado = form.cleaned_data["curso_asignado"]
            profesor.save()
            return redirect('myapp:profesores')
    else:
        form = ProfesorForm(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
            'curso_asignado': profesor.curso_asignado,
        })
    return render(request, 'myapp/profesor_formulario.html', {'form': form})

def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('myapp:profesores')
    return render(request, 'myapp/profesor_confirm_delete.html', {'profesor': profesor})


# --- TRABAJOS PRÁCTICOS ---

def trabajos_practicos(request):
    trabajos = TrabajoPractico.objects.all()
    return render(request, 'myapp/trabajos_practicos.html', {'trabajos': trabajos})

def crear_trabajo_practico(request):
    if request.method == 'POST':
        form = TrabajoPracticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:trabajos_practicos')
    else:
        form = TrabajoPracticoForm()
    return render(request, 'myapp/trabajo_practico_form.html', {'form': form})

def editar_trabajo_practico(request, pk):
    trabajo = get_object_or_404(TrabajoPractico, pk=pk)
    if request.method == 'POST':
        form = TrabajoPracticoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('myapp:trabajos_practicos')
    else:
        form = TrabajoPracticoForm(instance=trabajo)
    return render(request, 'myapp/trabajo_practico_form.html', {'form': form})

def eliminar_trabajo_practico(request, pk):
    trabajo = get_object_or_404(TrabajoPractico, pk=pk)
    if request.method == 'POST':
        trabajo.delete()
        return redirect('myapp:trabajos_practicos')
    return render(request, 'myapp/trabajo_practico_confirm_delete.html', {'trabajo': trabajo})

# --- DETALLE DEL TRABAJO (Para ver quién entregó) ---
def detalle_trabajo_practico(request, pk):
    trabajo = get_object_or_404(TrabajoPractico, pk=pk)
    entregas = trabajo.entregas.all()
    return render(request, 'myapp/trabajo_practico_detail.html', {'trabajo': trabajo, 'entregas': entregas})