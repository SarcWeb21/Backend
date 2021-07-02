from django.contrib import admin
from django.urls import path, include
from pmpportal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('step-one', views.step1, name='step1'),
    path('savedata', views.savedata, name='savedata'),
]