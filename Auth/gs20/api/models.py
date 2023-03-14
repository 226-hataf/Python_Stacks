from django.db import models


# Create your models here.
class Student(models.Model):
    email = models.CharField(max_length=100)
    passwowrd = models.IntegerField()
    city = models.CharField(max_length=100)
