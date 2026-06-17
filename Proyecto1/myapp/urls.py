from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiante/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
]