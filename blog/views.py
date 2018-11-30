# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Clap,Bookmark,Comment
from users.models import User
from datetime import datetime
# Create your views here.

def index(request):
    names=""
    posts = Post.objects.all()
    if request.session.get('email'):
        user = User.objects.get(email=request.session['email'])
        names=user.names
    context = {
        'posts': posts,
        'names':names
    }
    return render(request, "blog/index.html", context)

def detail(request):
    comments=None
    bookmarks=[]
    if request.GET.get('slug'):
        posts=Post.objects.get(slug=request.GET.get('slug'))
        commentaires=Comment.objects.filter(post_slug=request.GET.get('slug')).values()
        try:
            bookmarks_list=Bookmark.objects.get(post_slug=request.GET.get('slug'))
            if bookmarks_list.bookmarked:
                bookmarks_list.delete()
                bookmarks=[]
            bookmarks=bookmarks_list
        except Bookmark.DoesNotExist:
            bookmarks=[]
        comments=commentaires
        context={
        'post':posts,
        'comments':comments,
        'bookmarks':bookmarks
        }

        return render(request,"blog/details.html",context)
    else:
        return redirect('/posts')



def bookmark(request):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if request.GET.get('slug'):
            slug = request.GET.get('slug')
            try:
                bookmark = Bookmark.objects.get(user_id=user.user_id)
                if bookmark:
                    bookmark.delete()
            except Bookmark.DoesNotExist:
                new_bookmark = Bookmark(user_id=user.user_id, post_slug=slug,bookmarked=True)
                new_bookmark.save()
    return redirect('/details/?slug='+request.GET.get('slug'))

def posts(request):
    posts=Post.objects.all()
    context={
    'posts':posts
    }
    return render(request,"blog/posts.html",context)

def comment(request):
    if request.method=='POST':
        if 'email' in request.session:
            slug=request.GET.get('slug')
            user=User.objects.get(email=request.session['email'])
            comment=request.POST.get('comment')
            time=datetime.now().strftime('%a,%d %b %Y')
            new_comment=Comment(user_id=user.user_id,post_slug=slug,comment=comment,user_names=user.names,timestamp=time)
            new_comment.save()
            return redirect('/details/?slug='+slug)
        else:
            return redirect('/posts')
