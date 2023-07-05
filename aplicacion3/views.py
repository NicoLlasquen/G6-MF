from django.shortcuts import render, redirect
from .models import Usuario, Foro, Comentarios
from .form import Crear_comentario, Crear_usuario


def usuarios(request):

    todoUsuarios = Usuario.objects.all()

    return render(request, 'ap3/usuarios.html', {'usuarios': todoUsuarios})


def foro(request):

    todoForo = Foro.objects.all()

    return render(request, 'ap3/foro.html', {'foro': todoForo})


def comentarios(request):

    todoComentarios = Comentarios.objects.all()

    return render(request, 'ap3/comentarios.html', {'coment': todoComentarios})


def crearComentario(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearComentario.html', {'form': Crear_comentario})
    else:
        Comentarios.objects.create(
            texto=request.POST['texto'], usuarioComent=request.POST['usuario'])
        return redirect('comentario')


def crearUsuario(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearUsuario.html', {'form': Crear_usuario})
    else:
        Usuario.objects.create(nombre=request.POST['nombre'], rut=request.POST['rut'], añoAcad=request.POST['añoAcad'])
        return redirect('usuarios')
