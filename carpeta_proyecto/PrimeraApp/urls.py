from django.urls import path
from . import views  # 👈 para conectar con las vistas que luego crearás


   
urlpatterns = [
    path('', views.animales, name='index'),  # 👈 la vista de inicio
    path('animales/', views.animales, name='animales'),
    path('protectoras/', views.protectoras, name='protectoras'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
]
