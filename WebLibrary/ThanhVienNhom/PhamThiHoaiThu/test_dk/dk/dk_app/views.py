from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')  
        id_student = request.POST.get('id_student')  
        email = request.POST.get('email')
        password = request.POST.get('password')  # Đã sửa pass thành password

        new_user = User.objects.create_user(username=id_student, email=email, password=password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        # Sau khi đăng ký thành công, bạn có thể chuyển hướng đến trang khác hoặc thực hiện công việc khác ở đây.
        return redirect('/')  # Chuyển hướng đến trang chính sau khi đăng ký

    return render(request, 'register.html', {})
