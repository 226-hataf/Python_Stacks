from django.db import models



class User(models.Model):
    
    usernames = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.IntegerField()
    

