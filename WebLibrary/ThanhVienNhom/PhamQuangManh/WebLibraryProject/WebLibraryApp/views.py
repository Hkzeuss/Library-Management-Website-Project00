from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
# Create your views here.

def home(request):
    return render(request, "WebLibraryApp/Home.html")

def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "WebLibraryApp/Home.html", {"firstname": firstname})
        else:
            messages.error(request, "Can't Login")
            return redirect("home") 
    return render(request, "WebLibraryApp/Login.html")



def logout(request):
    return render(request, "WebLibraryApp/Logout.html")

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        raw_password = "new_password"
        password1 = make_password(raw_password)

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("login")

        

    return render(request, "WebLibraryApp/Register.html")