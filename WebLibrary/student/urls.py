from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ='home'),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name="forgot"),
    path('confirm/', views.confirm, name="confirm"),
    path('success/', views.success, name="success")
]