from django import forms
from .models import Usuario, Comentarios


class Crear_publicacion(forms.Form):
    titulo = forms.CharField(label="Titulo de la publicación", max_length=100)
    imagen = forms.ImageField(label="Imagen de la publicación")
    texto = forms.CharField(
        label="Contenido de la publicación", widget=forms.Textarea)
    # usu = Usuario.objects.get(id=1)


class Crear_comentario(forms.Form):
    texto = forms.CharField(label="Comentario", widget=forms.Textarea)
    # coment = Comentarios.objects.get(id=1)


class Crear_usuario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    rut = forms.IntegerField(label="Rut")
    año = forms.CharField(label="Año académico", max_length=50)
