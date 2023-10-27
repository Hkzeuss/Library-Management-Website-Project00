from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'student/home.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')  
        studentID = request.POST.get('studentID')  
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # Kiểm tra mật khẩu nhập lại
        if password != confirmPassword:
            messages.error(request, "Mật khẩu không khớp.")
            return redirect('register')

        # Tạo người dùng mới
        new_user = User.objects.create_user(username=studentID, email=email, password=password)
        new_user.first_name = firstName
        new_user.last_name = lastName
        new_user.save()
    
        # Thông báo thành công và chuyển hướng
        messages.success(request, "Đăng ký thành công.")
        return redirect('/')
    return render(request, 'student/register.html')

