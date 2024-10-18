from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

def userRegistration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, 
                    password=password
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'The passwords do not match')
            return redirect('register')

    return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('booklist')  
        else:
            messages.error(request, 'Invalid username or password')  
            return redirect('login')
    return render(request, 'login.html') 



def logoutView(request):
    logout(request)
    return redirect('login')

def homePage(request):
    return render(request, 'home.html')  




