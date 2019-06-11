from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200,default='user')

class user(models.Model):
    login = models.ForeignKey(login,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.PositiveIntegerField()
    place = models.CharField(max_length=200)

class hotel(models.Model):
    login = models.ForeignKey(login,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=200,default='pending')




