# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Admin(models.Model):
    names=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.names
