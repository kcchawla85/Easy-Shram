from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar = models.CharField(max_length=15)
    contact = models.CharField(max_length=13)

class UserLabour(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shramcard = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=15)
    contact = models.CharField(max_length=13)

class PostedJobs(models.Model):
    category = models.CharField(max_length=30)
    jobtitle = models.CharField(max_length=70)
    pay = models.CharField(max_length=7)
    age = models.CharField(max_length=3)
    contact = models.CharField(max_length=13)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)