from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/login")

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

def contact(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        problem = request.POST.get('problem')

        contact = Contact(name=name, email=email, address=address, problem=problem)
        contact.save()

    return render(request, 'contactus.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST.get('last_name')
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        # creat user 
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
    return render(request, 'signup.html')