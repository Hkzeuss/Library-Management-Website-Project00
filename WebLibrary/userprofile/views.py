from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .models import Profile
from .forms import ProfileForm
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def profile(request):
    return render(request, 'student/Profile.html')

@login_required(login_url='login')
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Hồ sơ của bạn đã được cập nhật!')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'student/EditProfile.html', context)
