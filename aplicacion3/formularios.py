from django import forms
from .models import Usuario, Comentarios


class Crear_publicacion(forms.Form):
    titulo = forms.CharField(label="Titulo de la publicación", max_length=100)
    texto = forms.CharField(
        label="Contenido de la publicación", widget=forms.Textarea)
    usuario = Usuario.objects.all()


class Crear_comentario(forms.Form):
    texto = forms.CharField(label="Comentario", widget=forms.Textarea)
    usuario = Comentarios.objects.all()


class Crear_usuario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    rut = forms.IntegerField(label="Rut", max_value=8, min_value=8)
    año = forms.CharField(label="Año académico", max_length=50)
