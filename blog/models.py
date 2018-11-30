# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Post(models.Model):
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    content = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to="images")
    posted_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Clap(models.Model):
    user_id = models.CharField(max_length=100)
    post_slug = models.CharField(max_length=100)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id +"---"+self.post_slug

class Bookmark(models.Model):
    user_id = models.CharField(max_length=100)
    post_slug = models.CharField(max_length=100)
    bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id+"---"+self.post_slug

class Comment(models.Model):
    user_id=models.CharField(max_length=100)
    post_slug=models.CharField(max_length=100)
    comment=models.TextField(max_length=1000)
    user_names=models.CharField(max_length=50)
    timestamp=models.CharField(max_length=50)

    def __str__(self):
        return self.comment
