from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .models import Profile
from student.models import Student
from .forms import ProfileForm
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from student.forms import StudentForm
from category.models import Category
from author.models import Author


# Create your views here.

def profile(request):
    categories = Category.objects.all()

    borrowed_books = request.session.get('borrowed_books', [])

    for book in borrowed_books:
        author_title = book.get('author', '')
        author = get_object_or_404(Author, title=author_title)
        book['author'] = author

    context = {
        'latest_categories': categories,
        'borrowed_books': borrowed_books,
    }
    user = request.user
    context['user'] = user
    return render(request, 'student/Profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    categories = Category.objects.all()
    context = {
            'latest_categories': categories,
        }
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile_instance = form.save(commit=False)
            
            try:
                student_instance = Student.objects.get(user=request.user)
            except Student.DoesNotExist:
                student_instance = Student(user=request.user)  # Tạo một bản ghi mới nếu chưa tồn tại.
            
            # Cập nhật trường 'first_name' trong 'User'
            student_instance.user.first_name = profile_instance.first_name
            student_instance.user.last_name = profile_instance.last_name
            student_instance.user.save()
            
            # Lưu thông tin mới của Profile
            if 'profile_img' in request.FILES:
                profile_instance.profile_img = request.FILES['profile_img']
                
            profile_instance.save()
            student_instance.save()
            
            messages.success(request, f'Hồ sơ của bạn đã được cập nhật!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    context['form'] = form

    return render(request, 'student/EditProfile.html', context)