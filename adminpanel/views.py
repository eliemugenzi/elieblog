# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Admin
from blog.models import Post
from django.utils.text import slugify
# Create your views here.

def index(request):
    names=""
    if 'admin' in request.session:
        admin=Admin.objects.get(email=request.session['admin'])
        names=user.names
    context={
    'names':names
    }
    return render(request,"adminpanel/index.html",context)

def new(request):
    if 'admin' in request.session:
        if request.method=='POST' and request.FILES['photo']:
            title=request.POST.get('title')
            description=request.POST.get('description')
            content=request.POST.get('content')
            category=request.POST.get('category')
            photo=request.FILES['photo']
            print(photo)
            slug=slugify(title)

            newpost=Post(slug=slug,title=title,description=description,content=content,photo=photo,category=category)
            newpost.save()
            return redirect('/cms/posts')
        return render(request,"adminpanel/new.html")
    else:
        return render(request,"adminpanel/unauthorized.html")

def delete(request):
    if 'admin' in request.session:
        if request.GET.get('slug'):
            slug=request.GET.get('slug')
            Post.objects.filter(slug=slug).delete()
            return redirect('/cms/posts')
        else:
            return redirect('/cms/posts')
    else:
        return render(request,"adminpanel/unauthorized.html")
def update(request):
    if request.method=='POST':
        title=request.POST.get('title')
        slug=slugify(title)
        description=request.POST.get('description')
        content=request.POST.get('content')
        category=request.POST.get('category')
        photo=None
        newblog=Post.objects.get(slug=request.GET.get('slug'))
        newblog.title=title
        newblog.slug=slug
        newblog.description=description
        newblog.content=content
        newblog.category=category
        if request.FILES['photo']:
            photo=request.FILES['photo']
            newblog.photo=photo
        newblog.save()
        return redirect('/cms/posts')
    slug=request.GET.get('slug')
    post=Post.objects.get(slug=slug)
    print(post.content)
    context={
    'post':post
    }
    return render(request,"adminpanel/update.html",context)
def login(request):
    error=""
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        admin=Admin.objects.filter(email=email,password=password)
        if admin:
            request.session['admin']=email
            return redirect('/cms/posts')
        else:
            error="Invalid Login Credentials"
    context={
    'error':error
    }
    return render(request,"adminpanel/login.html",context)
def register(request):
    error=""
    if request.method=='POST':
        names=request.POST.get('names')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm')

        if password!=confirm:
            error="Passwords must match!"
        else:
            admin=Admin(names=names,email=email,password=password)
            admin.save()
            request.session['admin']=email
            return redirect('/cms/posts')
    return render(request,"adminpanel/register.html")
def logout(request):
    if 'admin' in request.session:
        del request.session['admin']
    return redirect('/cms')
def posts(request):
    if 'admin' in request.session:
        posts=Post.objects.all()

        context={
        'posts':posts
        }
        return render(request,"adminpanel/posts.html",context)
    else:
        return render(request,"adminpanel/unauthorized.html")
