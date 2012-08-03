# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Entries(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Author = models.CharField(max_length=15, null=False)
    Contents = models.TextField(null=False)
    Writedate = models.DateTimeField(auto_now_add=True, auto_now=True)


    


