from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def login_user(request):
    """user login"""
    if request.method == 'GET':
        return render(request,'login.html',{})
    elif request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user = authenticate(username = user_name, password = pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        messages.error(request, 'Invalid username or password !!')
        return render(request,'login.html')




def user_logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    """signup page"""
    if request.method == 'GET':
        return render(request,'signup.html',{})
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password == re_password:
            userobj = User()
            userobj.first_name = name
            userobj.username = email
            userobj.set_password(password)
            userobj.save()
            user = authenticate(username = email, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        else:
            messages.error(request, 'Password and re enter password not match!!')
            return render(request,'signup.html')
