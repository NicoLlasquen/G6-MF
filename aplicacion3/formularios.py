from django import forms
from .models import Usuario, Comentarios


class Crear_publicacion(forms.Form):
    titulo = forms.CharField(label="Titulo de la publicación", max_length=100)
    texto = forms.Textarea()
    usuario = Usuario.objects.all()


class Crear_comentario(forms.Form):
    texto = forms.Textarea()
    usuario = Comentarios.objects.all()
