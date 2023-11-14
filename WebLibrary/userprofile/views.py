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
from borrow.models import Borrow
from book.models import Book


# Create your views here.

def profile(request):
    categories = Category.objects.all()

    # Retrieve borrowed books from the database
    borrowed_books = Borrow.objects.filter(user=request.user)

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
            if not form.cleaned_data['first_name'] or not form.cleaned_data['last_name']:
                messages.error(request, 'Vui lòng nhập đầy đủ họ và tên!')
                return render(request, 'student/EditProfile.html', {'form': form})
            profile_instance = form.save(commit=False)

            # Lấy hoặc tạo đối tượng Student
            student_instance, created = Student.objects.get_or_create(user=request.user)

            # Cập nhật các trường của User
            if created:
                student_instance.user.first_name = profile_instance.first_name
                student_instance.user.last_name = profile_instance.last_name
                student_instance.user.save()
                
            if form.has_changed():
                # Lấy danh sách các trường đã thay đổi
                changed_fields = form.changed_data

                # Lưu thông tin mới của Profile
                if 'profile_img' in changed_fields:
                    profile_instance.profile_img = request.FILES['profile_img']

                if 'last_name' in changed_fields or 'first_name' in changed_fields:
                    if 'last_name' in changed_fields:
                        profile_instance.last_name = form.cleaned_data['last_name']
                        student_instance.user.last_name = profile_instance.last_name
                    if 'first_name' in changed_fields:
                        profile_instance.first_name = form.cleaned_data['first_name']
                        student_instance.user.first_name = profile_instance.first_name

                if 'desc' in form.cleaned_data:  # Kiểm tra xem có giá trị desc không
                    profile_instance.desc = form.cleaned_data['desc']
                else:
                    profile_instance.profile_img = request.FILES['profile_img']

                profile_instance.save()

                user_update_fields = []
                if 'last_name' in changed_fields:
                    user_update_fields.append('last_name')
                if 'first_name' in changed_fields:
                    user_update_fields.append('first_name')
                student_instance.user.save(update_fields=user_update_fields)

                messages.success(request, 'Hồ sơ của bạn đã được cập nhật!')
                return redirect('profile')

    else:
        form = ProfileForm(instance=request.user.profile)

    context['form'] = form

    return render(request, 'student/EditProfile.html', context)