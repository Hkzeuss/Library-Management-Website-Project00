from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView, CategoryDeleteView, CategoryUpdateView, CategoryCreateView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

app_name = 'myadmin'
urlpatterns = [
     path('add_book/', BookCreateView.as_view(), name="add_book"),
     path('edit_book/<int:pk>/', BookUpdateView.as_view(), name="edit_book"),
     path('delete_book/<int:pk>/', BookDeleteView.as_view(), name="delete_book"),
     path('add_category/', CategoryCreateView.as_view(), name="add_category"),
     path('edit_category/<int:pk>/',
         CategoryUpdateView.as_view(), name="edit_category"),
     path('delete_category/<int:pk>/',
         CategoryDeleteView.as_view(), name="delete_category"),

     path('add_author/', AuthorCreateView.as_view(), name="add_author"),
     path('edit_author/<int:pk>/',
         AuthorUpdateView.as_view(), name="edit_author"),
     path('delete_author/<int:pk>/',
         AuthorDeleteView.as_view(), name="delete_author"),

]