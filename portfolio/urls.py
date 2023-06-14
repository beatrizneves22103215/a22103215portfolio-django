#  hello/urls.py

from django.urls import path
from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_view, name='apresentacao'),
    path('formacao', views.formacao_view, name='formacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('competencias', views.competencias_view, name='competencias'),
    path('nova', views.nova_page_view, name='nova'),
    path('edita/<int:post_id>/', views.editar_page_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_page_view, name='apaga'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('projetos', views.projetos_view, name='projetos'),
    path('competencias/', views.laboratorios_view, name='competencias'),
]

