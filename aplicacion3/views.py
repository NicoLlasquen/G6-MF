from django.shortcuts import render


def usuario(request):
    return render(request, 'ap3/usuario.html')
