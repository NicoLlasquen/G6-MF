from django.urls import path
from . import views

urlpatterns = [
    path('', views.pInicio, name='pInicio'),
    path('creditos/', views.creditos, name='creditos'),
    path('unidades/', views.unidades, name='unidades'),
]
