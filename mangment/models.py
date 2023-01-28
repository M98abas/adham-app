from django.db import models
from django.utils import timezone
from django import forms
class Admin(models.Model):
    email = models.EmailField(blank=True,unique=True)
    username = models.CharField(max_length=120,blank=True,unique=False)
    password = models.CharField(max_length=120)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email