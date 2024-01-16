from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),


    #Url de Inventario:
    
    path('clientes', views.clientes, name="clientes"),
]