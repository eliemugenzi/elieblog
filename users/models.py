# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_id=models.CharField(max_length=100)
    names=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.names
