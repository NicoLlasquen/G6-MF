from django.urls import path
from . import views

urlpatterns = [
    path('numeros/', views.numeros, name='numeros'),
    path('algebra/', views.algebra, name='algebra'),
    path('geometria/', views.geometria, name='geometria'),
    path('probabilidad/', views.probabilidades, name='probabilidad'),
]
