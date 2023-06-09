from django.shortcuts import render


def pInicio(request):
    return render(request, 'ap1/pInicio.html')


def creditos(request):
    return render(request, 'ap1/Creditos.html')


def unidades(request):
    return render(request, 'ap1/unidades.html')
