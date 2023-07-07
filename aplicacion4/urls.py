from django.urls import path
from . import views

urlpatterns = [
    path('ForoNumeros/', views.foroNumeros, name='foroNumeros'),
    path('ForoAlgebra/', views.foroAlgebra, name='foroAlgebra'),
    path('ForoGeometria/', views.foroGeometria, name='foroGeometria'),
    path('ForoProbabilidad/', views.foroProbabilidad, name='foroProbabilidad'),
]
