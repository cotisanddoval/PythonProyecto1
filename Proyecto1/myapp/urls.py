from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),

    # Estudiantes
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # Cursos
    path('cursos/', views.cursos, name='cursos'),
    path('curso/nuevo/', views.cursoFormulario, name='cursoFormulario'),

    # Profesores
    path('profesores/', views.profesores, name='profesores'),
    path('profesor/nuevo/', views.profesorFormulario, name='profesorFormulario'),

    # Entregables
    path('entregables/', views.entregables, name='entregables'),
]