from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.IntegerField()
    añoAcad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Foro(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    usuarioForo = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + "-" + self.usuarioForo.nombre


class Comentarios(models.Model):
    texto = models.TextField()
    usuarioComent = models.ForeignKey(Usuario, on_delete=models.CASCADE)
