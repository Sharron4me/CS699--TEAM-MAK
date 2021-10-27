from django.db import models

class student(models.Model):
    '''Model has the following atributes and is used to store student Info
    1)  ldap ID
    2)  Name
    3)  password
    4)  Verification Code
    5)  Account Status
    '''
    ldap = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

class admintable(models.Model):
    '''Model is used to store admin info and has the following atributes
        1)  user_name
        2)  Name
        3)  password
    '''
    ldap = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

# Create your models here.
