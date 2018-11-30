# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Clap,Bookmark,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Clap)
admin.site.register(Bookmark)
admin.site.register(Comment)
