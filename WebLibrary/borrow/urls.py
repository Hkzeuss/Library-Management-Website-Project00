from django.urls import path
from .views import BorrowListView, BorrowDetailView
app_name = 'borrow'
urlpatterns = [
    path('', BorrowListView.as_view(), name='borrow'),
    path('borrow/<int:pk>', BorrowDetailView.as_view(), name='detail'),
]