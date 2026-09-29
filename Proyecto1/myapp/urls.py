from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # Inicio
    path('', views.index, name='index'),

    # Estudiantes
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('mi-panel/', views.panel_alumno, name='panel_alumno'),

    # Cursos
    path('cursos/', views.cursos, name='cursos'),
    path('curso/nuevo/', views.cursoFormulario, name='cursoFormulario'),
    path('cursos/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),

    # Profesores
    path('profesores/', views.profesores, name='profesores'),
    path('profesores/crear/', views.profesorFormulario, name='profesorFormulario'),
    path('profesores/editar/<int:pk>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:pk>/', views.eliminar_profesor, name='eliminar_profesor'),

    # Trabajos Prácticos
    path('trabajos/', views.trabajos_practicos, name='trabajos_practicos'),
    path('trabajos/crear/', views.crear_trabajo_practico, name='crear_trabajo_practico'),
    path('trabajos/<int:pk>/', views.detalle_trabajo_practico, name='detalle_trabajo_practico'),
    path('trabajos/editar/<int:pk>/', views.editar_trabajo_practico, name='editar_trabajo_practico'),
    path('trabajos/eliminar/<int:pk>/', views.eliminar_trabajo_practico, name='eliminar_trabajo_practico'),
    path('trabajos/<int:tp_id>/entregar/', views.subir_entrega, name='subir_entrega'),
    path('entregas/<int:pk>/calificar/', views.calificar_entrega, name='calificar_entrega'),
]
