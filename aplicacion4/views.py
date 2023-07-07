from django.shortcuts import render


def foroNumeros(request):
    return render(request, 'ap4/foroNumeros.html')


def foroAlgebra(request):
    return render(request, 'ap4/foroAlgebra.html')


def foroGeometria(request):
    return render(request, 'ap4/foroGeometria.html')


def foroProbabilidad(request):
    return render(request, 'ap4/foroProbabilidad.html')
