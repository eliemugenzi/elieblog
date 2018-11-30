# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
import uuid
import hashlib

# Create your views here.

def signin(request):
    error=""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_hash = hashlib.sha224(password).hexdigest()
        try:
            user = User.objects.get(email=email, password=password_hash)
            if user:
                request.session['email'] = email
                return redirect('/')
            else:
                error = "Invalid Username or Password"
        except User.DoesNotExist:
            error="Invalid Username or Password"
    context = {
        'error':error
    }
    return render(request, "users/login.html",context)

def register(request):
    error=""
    if request.method == 'POST':
        names = request.POST.get('names')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        user = User.objects.filter(email=email)
        if password != confirm:
            error = "Passwords must Match"
        elif user:
            error="Email Already exist!"

        else:
            x = uuid.uuid4()
            user_id = str(x)
            password_hash=hashlib.sha224(password).hexdigest()
            user = User(user_id=user_id, names=names, email=email, password=password_hash)
            user.save()
            request.session['email'] = email
            return redirect('/')

    context = {
        'error':error
    }
    return render(request, "users/register.html", context)

def logout(request):
    del request.session['email']
    return redirect('/')
