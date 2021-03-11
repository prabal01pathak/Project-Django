from django.db import models


class SignUp(models.Model):
    first_Name = models.CharField(max_length=10,blank= False)
    last_Name = models.CharField(max_length=10,blank = False)
    Email = models.EmailField(max_length = 230)
    password = models.CharField(max_length = 33)

class LogIn(models.Model):
    Email = models.EmailField(max_length=22)
    password = models.CharField(max_length = 22)
    
 
