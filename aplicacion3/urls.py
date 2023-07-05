from django.urls import path
from . import views


urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('Foro/', views.foro, name='foro'),
    path('Comentarios/', views.comentarios, name='comentario'),
    path('CrearComentario/', views.crearComentario, name='crearComentario'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario')
]
