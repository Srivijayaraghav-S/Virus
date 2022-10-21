from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StudentUser(AbstractUser):
  pass

class Students(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=6)
    branch = models.CharField(max_length=5)
    section = models.CharField(max_length=5)

class Recruiters(models.Model):
  compname=models.CharField(max_length=64)
  recruitername=models.CharField(max_length=64)
  compemail=models.EmailField(max_length=64)
  complink=models.URLField(max_length=64)
