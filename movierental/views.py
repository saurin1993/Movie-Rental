from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth import logout

def homepage(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if User.objects.filter(username=username).exists():
            auth_login(request, user)
            return redirect("movie_all")

        else:
            return HttpResponse("<h1>Username or Password Doesn't match. Please try again </h1>")
    else:
        return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('homepage')



def login(request):
    return render(request,'login.html')

