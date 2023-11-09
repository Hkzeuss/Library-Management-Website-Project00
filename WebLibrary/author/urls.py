from django.urls import path
from .views import AuthorListView, AuthorDetailView
app_name = 'author'
urlpatterns = [
    path('', AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='detail'),
]