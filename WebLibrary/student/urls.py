from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ='home'),
    path('home1/', views.homefanpage, name='homefanpage'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.signout, name='logout'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name="forgot"),
    path('confirm/', views.confirm, name="confirm"),
    path('success/', views.success, name="success")
]