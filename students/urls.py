from django.contrib import admin
from django.urls import path, include
from . import views.

urlpatterns = [

    path('create', views.create, name='create'),
    path('home', views.home, name='home')
    path('search', views.home, name='home')
    path('<int:student_id>', views.detail, name='detail')
]
