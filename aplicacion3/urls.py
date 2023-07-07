from django.urls import path
from . import views


urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('Sugerencias/', views.sugerencias, name='sugerencias'),
    path('CrearSugerencia/', views.crearSugerencia, name='crearSugerencia'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario')
]
