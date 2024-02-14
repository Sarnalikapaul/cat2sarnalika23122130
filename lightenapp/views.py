from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "lighten/index.html")

def about(request):
    return render(request, 'lighten/aboutus.html')


def product(request):
    return render(request, 'lighten/product.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the 'index' page upon successful login
        else:
            return render(request, 'lighten/login.html')

    return render(request, 'lighten/login.html')

def register_user(request):
    if request.method == "POST":
        vemail = request.POST.get('email')
        vfirst_name = request.POST.get('first_name')
        vlast_name = request.POST.get('last_name')
        vpassword = request.POST.get('password')
        vgender = request.POST.get('gender')

        # Check if vemail is not empty
        if not vemail:
            return render(request, 'lighten/register.html', {'error': 'Email is required'})

        myuser = User.objects.create_user(username=vemail, email=vemail, password=vpassword)
        myuser.save()

        new_user = UserProfile(
            user=myuser,
            email=vemail,
            first_name=vfirst_name,
            last_name=vlast_name,
            gender=vgender
        )
        new_user.save()

        return render(request, 'lighten/login.html')

    return render(request, 'lighten/register.html')



def student(request):
    if request.method == "POST":
        vname = request.POST.get('fname')  # Consider using a more secure method like hashing
        vage = request.POST.get('age')
    

        new_student = StudentProfile(
            name=vname,
            age=vage
        )
        new_student.save()

        return render(request, 'lighten/student.html')

    return render(request, 'lighten/student.html')
