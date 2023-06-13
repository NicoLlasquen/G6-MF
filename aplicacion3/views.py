from django.shortcuts import render, redirect
from .models import Usuario, Foro, Comentarios
from .formularios import Crear_publicacion, Crear_comentario


def usuarios(request):

    todoUsuarios = Usuario.objects.all()

    return render(request, 'ap3/usuarios.html', {'usuarios': todoUsuarios})


def foro(request):

    todoForo = Foro.objects.all()

    return render(request, 'ap3/foro.html', {'foro': todoForo})


def comentarios(request):

    todoComentarios = Comentarios.objects.all()

    return render(request, 'ap3/comentarios.html', {'coment': todoComentarios})


def crearForo(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearForo.html', {'form': Crear_publicacion})
    else:
        Foro.objects.create(
            titulo=request.POST['titulo'], texto=request.POST['texto'], usuario=request.POST['usuario'])
        return redirect('foro')


def crearComentario(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearComentario.html', {'form': Crear_comentario})
    else:
        Comentarios.objects.create(texto=request.POST['texto'])
        return redirect('comentario')
