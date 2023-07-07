from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.IntegerField()
    añoAcad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tematica(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="static/imagenes/foro")

    def __str__(self):
        return self.nombre


class Numeros(Tematica):
    documentos = models.FileField(storage="static/documentos/numeros")


class Algebra(Tematica):
    documentos = models.FileField(storage="static/documentos/algebra")


class Geometria(Tematica):
    documentos = models.FileField(storage="static/documentos/geometria")


class Probabilidad(Tematica):
    documentos = models.FileField(storage="static/documentos/probabilidad")


class Sugerencias(models.Model):
    texto = models.TextField()
    usuarioSugerencia = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuarioSugerencia.nombre


class Comentarios(models.Model):
    texto = models.TextField(max_length=300)
    usuarioComentario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuarioComentario.nombre
