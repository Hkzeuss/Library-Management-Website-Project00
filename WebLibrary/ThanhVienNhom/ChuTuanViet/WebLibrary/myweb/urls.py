from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.signup, name='sign_up'),
    # thêm các URL khác của ứng dụng tại đây
]
