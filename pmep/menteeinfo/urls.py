from django.contrib import admin
from django.urls import path, include
from menteeinfo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mentors/register/', views.register),
    path('registration/', views.registrations)   
]