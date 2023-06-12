from django.shortcuts import render
from .models import Usuario


def usuarios(request):

    todoUsuarios = Usuario.objects.all()

    return render(request, 'ap3/usuarios.html', {'usuarios': todoUsuarios})
