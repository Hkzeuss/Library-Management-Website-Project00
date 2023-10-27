from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
]
