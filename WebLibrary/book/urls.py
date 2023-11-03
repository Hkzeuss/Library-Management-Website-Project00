from django.urls import path
from . import views
from django.urls import path
from .views import HomeListView, BookDetailView, BorrowBtn, ReturnBtn, Search, BookListView
app_name = 'book'
urlpatterns = [
    path('', HomeListView.as_view(), name='book'),
    path('books/', BookListView.as_view(), name='list_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('borrow/<int:pk>', BorrowBtn.as_view(), name='book_borrow'),
    path('return/<int:pk>', ReturnBtn.as_view(), name='book_return'),
    path('search/', Search.as_view(), name='search'),
    
    path('tabrules/',views.tabrules, name='tabrules'),
    path('bookcase/', views.bookcase, name ='bookcase'),
    path('hitstory/', views.hitstory, name='hitstory'),
    path('hitstory_6/', views.hitstory_6, name='hitstory_6'),
    path('hitstory_7/', views.hitstory_7, name='hitstory_7'),
    path('hitstory_8/', views.hitstory_8, name='hitstory_8'),
    path('hitstory_9/', views.hitstory_9, name='hitstory_9'),
    path('geography/',views.geography, name='geography'),
    path('geography_6/',views.geography_6, name='geography_6'),
    path('geography_7/',views.geography_7, name='geography_7'),
    path('geography_8/',views.geography_8, name='geography_8'),
    path('geography_9/',views.geography_9, name='geography_9'),
    path('education/',views.education, name='education'),
    path('education_6/',views.education_6, name='education_6'),
    path('education_7/',views.education_7, name='education_7'),
    path('education_8/',views.education_8, name='education_8'),
    path('education_9/',views.education_9, name='education_9'),
    path('english/',views.english, name='english'),
    path('english_6/',views.english_6, name='english_6'),
    path('english_7/',views.english_7, name='english_7'),
    path('english_8/',views.english_8, name='english_8'),
    path('english_9/',views.english_9, name='english_9'),
    path('introduce/',views.introduce, name='introduce')

]