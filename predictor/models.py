from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
