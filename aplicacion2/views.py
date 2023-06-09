from django.shortcuts import render


def numeros(request):
    return render(request, 'ap2/numeros.html')


def algebra(request):
    return render(request, 'ap2/algebra.html')


def geometria(request):
    return render(request, 'ap2/geometria.html')


def probabilidades(request):
    return render(request, 'ap2/probabilidad.html')
