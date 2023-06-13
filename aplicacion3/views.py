from django.shortcuts import render
from .models import Usuario, Foro, Comentarios


def usuarios(request):

    todoUsuarios = Usuario.objects.all()

    return render(request, 'ap3/usuarios.html', {'usuarios': todoUsuarios})


def foro(request):

    todoForo = Foro.objects.all()

    return render(request, 'ap3/foro.html', {'foro': todoForo})


def comentarios(request):

    todoComentarios = Comentarios.objects.all()

    return render(request, 'ap3/comentarios.html', {'coment': todoComentarios})
