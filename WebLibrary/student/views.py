from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'student/home.html')

def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate( username=username, password=password)

        if user is not None:
            login(request, user)
            firstName = user.first_name
            return render(request, "student/home.html", {"firstName": firstName})
        else:
            messages.error(request, "Can't Login")
            
            return redirect('/') 
    return render(request, "student/Login.html")

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

def forgot(request):
    return render(request, 'student/ForgotPassword.html')

def confirm(request):
    return render(request, 'student/ConfirmForgotPassword.html')

def success(request):
    return render(request, 'student/succsesforgotpassword.html')
