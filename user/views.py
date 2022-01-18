from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutUs.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect("/login")