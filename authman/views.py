# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate

from .forms import UserSignupForm
from . import commands


def signup(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            form = UserSignupForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user_type = form.cleaned_data['user_type']
                user = User.objects.get(username=username)
                commands.add_users_to_group(user, user_type)
                messages.info(request, 'user created successfully!')
                return redirect('authman:signup')
            else:
                print(form.errors)
                messages.error(request, form.errors)
                return redirect('authman:signup')
        return redirect('home:home')
    else:
        form = UserSignupForm()
        return render(request, 'authman/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Login succesful")
            return redirect('home:home')
        else:
            messages.error(request, "invalid username or password")
            return redirect('authman:login')    
    else:
        authentication_form = AuthenticationForm()
        return render(request, 'authman/login.html', {'form': authentication_form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logout succesful")
    return redirect('home:home')
    # Redirect to a success page