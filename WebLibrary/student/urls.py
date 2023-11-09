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
    path('reset/<str:token>/', views.reset, name="reset"),
    path('success/', views.success, name="success"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.edit_profile, name="editprofile")
]