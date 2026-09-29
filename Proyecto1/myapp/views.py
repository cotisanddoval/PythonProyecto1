from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Estudiante, Profesor, Curso, TrabajoPractico, Entrega
from .forms import CursoFormulario, ProfesorForm, EstudianteForm, TrabajoPracticoForm, EntregaForm
from accounts.models import Perfil

@login_required
def subir_entrega(request, tp_id):
    trabajo = get_object_or_404(TrabajoPractico, id=tp_id)
    
    # Vinculamos correctamente el estudiante con el usuario actual o su correo
    estudiante = Estudiante.objects.filter(email=request.user.email).first()
    if not estudiante:
        estudiante = Estudiante.objects.first() 

    entrega, created = Entrega.objects.get_or_create(
        trabajo_practico=trabajo,
        estudiante=estudiante
    )
    
    if request.method == 'POST':
        form = EntregaForm(request.POST, request.FILES, instance=entrega)
        if form.is_valid():
            entrega_guardada = form.save(commit=False)
            entrega_guardada.trabajo_practico = trabajo
            entrega_guardada.estudiante = estudiante
            entrega_guardada.entregado = True
            entrega_guardada.save()
            return redirect('myapp:detalle_curso', curso_id=trabajo.curso.id)
    else:
        form = EntregaForm(instance=entrega)
        
    return render(request, 'myapp/subir_entrega.html', {'form': form, 'trabajo': trabajo})

@login_required
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    trabajos = TrabajoPractico.objects.filter(curso=curso)
    
    return render(request, 'myapp/detalle_curso.html', {
        'curso': curso,
        'trabajos': trabajos,
    })

# --- CANDADOS DE SEGURIDAD ---

def solo_admin(view_func):
    """Permite el acceso solo si el usuario logueado es Administrador."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'perfil') and request.user.perfil.rol == 'admin':
            return view_func(request, *args, **kwargs)
        return redirect('myapp:index')
    return wrapper

def profesor_o_admin(view_func):
    """Permite el acceso a Profesores y Administradores."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'perfil') and request.user.perfil.rol in ['admin', 'profesor']:
            return view_func(request, *args, **kwargs)
        return redirect('myapp:panel_alumno')
    return wrapper

def index(request):
    return render(request, 'myapp/index.html')

# --- ESTUDIANTES ---

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes.html', {'estudiantes': estudiantes})

@login_required
def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    
    entregas = Entrega.objects.filter(estudiante=estudiante)
    cursos_ids = entregas.values_list('trabajo_practico__curso', flat=True).distinct()
    cursos = Curso.objects.filter(id__in=cursos_ids)

    return render(request, 'myapp/estudiante_detail.html', {
        'estudiante': estudiante,
        'entregas': entregas,
        'cursos': cursos,
    })

@solo_admin
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Este nombre de usuario ya está en uso. Elige otro.')
                return render(request, 'myapp/estudiante_form.html', {'form': form})
            
            user = User.objects.create_user(username=username, email=email, password=password)
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.rol = 'alumno'
            perfil.save()
            
            form.save()
            return redirect('myapp:estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiante_form.html', {'form': form})

@solo_admin
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

@solo_admin
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

@profesor_o_admin
def cursoFormulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:cursos')
    else:
        form = CursoFormulario()
       
    return render(request, 'myapp/curso_formulario.html', {'form': form})

@profesor_o_admin
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

@profesor_o_admin
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('myapp:cursos')
    return render(request, 'myapp/curso_confirm_delete.html', {'curso': curso})


# --- PROFESORES ---

@solo_admin
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})

@solo_admin
def profesorFormulario(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Este nombre de usuario ya está en uso. Elige otro.')
                return render(request, 'myapp/profesor_form.html', {'form': form})
            
            user = User.objects.create_user(username=username, email=email, password=password)
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.rol = 'profesor'
            perfil.save()
            
            form.save()
            return redirect('myapp:profesores')
    else:
        form = ProfesorForm()
    return render(request, 'myapp/profesor_form.html', {'form': form})

@solo_admin
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

@solo_admin
def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('myapp:profesores')
    return render(request, 'myapp/profesor_confirm_delete.html', {'profesor': profesor})


# --- TRABAJOS PRÁCTICOS ---

@profesor_o_admin
def trabajos_practicos(request):
    trabajos = TrabajoPractico.objects.all()
    return render(request, 'myapp/trabajos_practicos.html', {'trabajos': trabajos})

@profesor_o_admin
def crear_trabajo_practico(request):
    if request.method == 'POST':
        form = TrabajoPracticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:trabajos_practicos')
    else:
        form = TrabajoPracticoForm()
    return render(request, 'myapp/trabajo_practico_form.html', {'form': form})

@profesor_o_admin
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

@profesor_o_admin
def eliminar_trabajo_practico(request, pk):
    trabajo = get_object_or_404(TrabajoPractico, pk=pk)
    if request.method == 'POST':
        trabajo.delete()
        return redirect('myapp:trabajos_practicos')
    return render(request, 'myapp/trabajo_practico_confirm_delete.html', {'trabajo': trabajo})

@profesor_o_admin
def detalle_trabajo_practico(request, pk):
    trabajo = get_object_or_404(TrabajoPractico, pk=pk)
    entregas = trabajo.entregas.all()
    return render(request, 'myapp/trabajo_practico_detail.html', {'trabajo': trabajo, 'entregas': entregas})

@profesor_o_admin
def calificar_entrega(request, pk):
    entrega = get_object_or_404(Entrega, pk=pk)
    if request.method == 'POST':
        nota_str = request.POST.get('nota')
        if nota_str:
            try:
                # Intentamos convertir la nota a número entero (o float si usas decimales)
                entrega.nota = int(nota_str)
                entrega.save()
                return redirect('myapp:detalle_trabajo_practico', pk=entrega.trabajo_practico.pk)
            except ValueError:
                # Si el usuario ingresa algo inválido, puedes manejarlo o mostrar un error
                form_error = "Por favor, ingresa un número válido para la nota."
                return render(request, 'myapp/calificar_entrega.html', {'entrega': entrega, 'error': form_error})
                
    return render(request, 'myapp/calificar_entrega.html', {'entrega': entrega})


# --- PANEL DEL ALUMNO ---

@login_required
def panel_alumno(request):
    estudiante = Estudiante.objects.filter(email=request.user.email).first()
    
    if estudiante:
        entregas = Entrega.objects.filter(estudiante=estudiante)
        cursos_ids = entregas.values_list('trabajo_practico__curso', flat=True).distinct()
        cursos = Curso.objects.filter(id__in=cursos_ids)
    else:
        entregas = []
        cursos = []

    return render(request, 'myapp/estudiante_detail.html', {
        'estudiante': estudiante,
        'entregas': entregas,
        'cursos': cursos,
    })