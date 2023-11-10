from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tabrules/',views.tabrules, name='tabrules'),
    path('introduce/',views.introduce, name='introduce'),
    path('booklib/', views.booklib, name="booklib"),
    path('category_detail/<int:pk>/', views.category_detail, name='category_detail'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/', views.book_detail, name="book_detail"),
    path('view_pdf/<int:pk>/', views.book_detail, name="view_pdf"),
    path('author_detail/<int:pk>/', views.author_detail, name='author_detail'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
