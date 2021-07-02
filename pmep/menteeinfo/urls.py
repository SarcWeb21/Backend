from django.contrib import admin
from django.urls import path, include
from menteeinfo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register1', views.register1, name = 'register1'),
    path('register2', views.register2, name = 'register2')
]