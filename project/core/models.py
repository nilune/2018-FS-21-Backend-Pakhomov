# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    pass
