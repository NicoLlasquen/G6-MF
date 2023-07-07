from django.shortcuts import render, redirect
from .models import Usuario, Sugerencias
from .form import Crear_sugerencia, Crear_usuario


def usuarios(request):

    todoUsuarios = Usuario.objects.all()

    return render(request, 'ap3/usuarios.html', {'usuarios': todoUsuarios})


def sugerencias(request):

    todoSugerencias = Sugerencias.objects.all()

    return render(request, 'ap3/sugerencias.html', {'coment': todoSugerencias})


def crearSugerencia(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearSugerencia.html', {'form': Crear_sugerencia})
    else:
        Sugerencias.objects.create(
            texto=request.POST['texto'], usuarioComent=request.POST['usuario'])
        return redirect('comentario')


def crearUsuario(request):

    if request.method == 'GET':
        return render(request, 'ap3/crearUsuario.html', {'form': Crear_usuario})
    else:
        Usuario.objects.create(nombre=request.POST['nombre'], rut=request.POST['rut'], añoAcad=request.POST['añoAcad'])
        return redirect('usuarios')
