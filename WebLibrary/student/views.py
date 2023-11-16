from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .models import OTP
from .forms import LoginForm
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from userprofile.views import profile, edit_profile
from category.models import Category

def home(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, 'student/home.html', context)

def homefanpage(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, 'student/homefanpage.html', context)

@user_passes_test(lambda u: not u.is_authenticated, login_url='homefanpage')
def loginPage(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
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
                form.add_error(None, "Bạn đã nhập sai tài khoản hoặc mật khẩu")
                messages.error(request, "Xin vui lòng nhập lại")

    else:
        form = LoginForm()

    context['form'] = form

    return render(request, "student/Login.html", context)

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
        
        email_prefix = email.split('@')[0]
        if email_prefix != studentID:
            error_messages['email_prefix_mismatch'] = "Đầu email phải giống với Student ID"

        # Kiểm tra kích thước mật khẩu
        if not 8 <= len(password) <=16:
            if len(password) < 8:
                error_messages['password_length_min'] = "Mật khẩu tối thiểu 8 ký tự"
            elif len(password) > 16:
                error_messages['password_length_max'] = "Mật khẩu tối đa 16 ký tự"
                


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
        return redirect('login')
    
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }

    return render(request, 'student/register.html', context)

def signout(request):
    logout(request)
    return redirect('/')

def forgot(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get("email")
        username = request.POST.get("username")
        
        # Kiểm tra xem username và email đã được nhập hay chưa
        if not username:
            messages.error(request, "Tên người dùng không được bỏ trống.")
            return redirect("forgot")

        if not email:
            messages.error(request, "Email không được bỏ trống.")
            return redirect("forgot")

        try:
            user = User.objects.get(username=username, email=email)
            otp = str(random.randint(100000, 999999))
            OTP.objects.create(user=user, token=otp)
            subject = "Tài khoản của bạn sẽ được đổi mật khẩu khi bạn nhập OTP"
            message = f"Chào bạn {username} thân mến,\n\nChúng tôi rất vui mừng thông báo về một sự kiện đặc biệt trên tài khoản của bạn tại Thư viện VJULIB.\n\nĐể đảm bảo an toàn và bảo mật cho bạn, chúng tôi đã gửi một Mã OTP đặc biệt. Hãy nhập mã này sau khi bạn đăng nhập:\n\nMã OTP: {otp}\n\nNếu đây không phải là bạn, xin đừng lo lắng. Bạn có thể bỏ qua thông báo này hoặc liên hệ ngay với chúng tôi. Chúng tôi sẵn sàng hỗ trợ bạn ngay lập tức và giải đáp mọi thắc mắc.\n\nChúng tôi xin gửi lời cảm ơn sâu sắc nhất đến bạn vì đã tin tưởng và lựa chọn sử dụng dịch vụ của Thư viện VJULIB.\n\nNếu có bất kỳ câu hỏi hoặc nhu cầu hỗ trợ nào khác, Đội Ngũ VJULIB luôn sẵn lòng để giúp đỡ bạn.\n\nTrân trọng,\nĐội Ngũ VJULIB"
            from_email = 'vjulib@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("confirm")
        except User.DoesNotExist:
            messages.error(request, "Không tìm thấy tài khoản với thông tin bạn nhập.")
            return redirect("forgot")
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, "student/ForgotPassword.html", context)

def confirm(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        try:
            reset_request = OTP.objects.get(token=otp)
            if reset_request.token == otp:
                return redirect('reset', token=reset_request.token)
            else:
                messages.error(request, "Mã OTP không hợp lệ.")
        except OTP.DoesNotExist:
            messages.error(request, "Mã OTP không hợp lệ.")
    
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, 'student/ConfirmForgotPassword.html', context)


def reset(request, token):
    categories = Category.objects.all()
    print(categories)
    context={}
    try:
        OTP_user = OTP.objects.filter(token = token).first()

        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            user_id = request.POST.get("user_id")
            
            if user_id is None:
                messages.error(request, "Không tìm thấy thông tin người dùng")
                return redirect('reset', token=token)
            if new_password != confirm_password:
                messages.error(request, "Xin vui lòng nhập lại")
                return redirect('reset', token=token)
            
            # Kiểm tra kích thước mật khẩu
            if not 8 <= len(new_password) <= 16:
                if len(new_password) < 8:
                    messages.error(request, "Mật khẩu tối thiểu 8 ký tự")
                elif len(new_password) > 16:
                    messages.error(request, "Mật khẩu tối đa 16 ký tự")
                return redirect('reset', token=token)
        
            User_obj = User.objects.get(id=user_id)
            User_obj.set_password(new_password)
            User_obj.save()
            return redirect('success')
        context = {
            'user_id': OTP_user.user.id,
            'latest_categories': categories,
            }
    except Exception as e:
        print(e)
    return render(request, 'student/ResetPassword.html', context)

def success(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'latest_categories': categories,
    }
    return render(request, 'student/succsesforgotpassword.html', context)

