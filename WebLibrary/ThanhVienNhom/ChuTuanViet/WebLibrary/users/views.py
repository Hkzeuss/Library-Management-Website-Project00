from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            student_id = form.cleaned_data['student_id']
            password = form.cleaned_data['password']

            # Lưu thông tin người dùng vào cơ sở dữ liệu
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                student_id=student_id,
                password=password
            )

            return redirect('/')  
    else:
        form = RegistrationForm()
    return render(request, 'users/sign_up.html', {'form': form})



