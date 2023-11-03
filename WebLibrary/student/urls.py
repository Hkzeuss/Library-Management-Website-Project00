from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('home1/profile/', views.profile, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)