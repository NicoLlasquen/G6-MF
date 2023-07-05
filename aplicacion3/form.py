from django import forms
from .models import Usuario


class Crear_comentario(forms.Form):
    texto = forms.CharField(label="Comentario", widget=forms.Textarea)
    # usuarioComent = Usuario.objects.filter(rut__in=nombre)


class Crear_usuario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    rut = forms.IntegerField(label="Rut")
    añoAcad = forms.CharField(label="Año académico", max_length=50)
