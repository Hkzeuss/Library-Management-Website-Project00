from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profiles'
urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('editprofile', views.edit_profile, name="editprofile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)