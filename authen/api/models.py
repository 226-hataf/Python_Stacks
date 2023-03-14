from django.db import models

# Create your models here.

class Users (models.Model):
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.IntegerField()
    email = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name