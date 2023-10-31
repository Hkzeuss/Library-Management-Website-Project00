from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import LoginForm


def home(request):
    return render(request, 'student/home.html')

def homefanpage(request):
    return render(request, 'student/homefanpage.html')

@user_passes_test(lambda u: not u.is_authenticated, login_url='homefanpage')
def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homefanpage') 
            else:
                form.add_error(None, "Bạn đã nhập sai tài khoản hoặc mật khẩu. Xin vui lòng thử lại")

    else:
        form = LoginForm()

    return render(request, "student/Login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')  
        studentID = request.POST.get('studentID')  
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # Tạo từ điển tróng
        error_messages = {}

        # Kiểm tra các trường dữ liệu để tìm ra dữ liệu đang bỏ trống
        if not firstName:
            error_messages['firstName'] = "None"
        if not lastName:
            error_messages['lastName'] = "None"
        if not studentID:
            error_messages['studentID'] = "None"
        if not email:
            error_messages['email'] = "None"
        if not password:
            error_messages['password'] = "None"
        if not confirmPassword:
            error_messages['confirmPassword'] = "None"

        # Kiểm tra Student ID và email xem đã tồn tại chưa
        if User.objects.filter(username=studentID).exists():
            error_messages['studentID_exists'] = "Student ID đã tồn tại!"

        if User.objects.filter(email=email).exists():
            error_messages['email_exists'] = "Email đã tồn tại!"

        # Kiểm tra định dạng email
        if not email.endswith('@st.vju.ac.vn'):
            error_messages['invalid_email'] = "'@st.vju.ac.vn'"

        # Kiểm tra mật khẩu có khớp không
        if password != confirmPassword:
            error_messages['password_mismatch'] = "Mật khẩu không khớp!"

        # Quay lại trang đăng ký nếu xảy ra lỗi và hiển thị lỗi
        if error_messages:
            return render(request, 'student/register.html', {'error_messages':  error_messages, 'input_data': request.POST})


        # Tạo người dùng mới
        new_user = User.objects.create_user(username=studentID, email=email, password=password)
        new_user.first_name = firstName
        new_user.last_name = lastName
        new_user.save()
    
        # Thông báo thành công và chuyển hướng
        messages.success(request, "Đăng ký thành công.")
        return redirect('/login')

    return render(request, 'student/register.html')

def signout(request):
    logout(request)
    return redirect('/')

def forgot(request):

    return render(request, 'student/ForgotPassword.html')

def confirm(request):
    return render(request, 'student/ConfirmForgotPassword.html')

def success(request):
    return render(request, 'student/succsesforgotpassword.html')
