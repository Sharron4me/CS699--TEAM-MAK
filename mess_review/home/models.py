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

class waste(models.Model):
    '''Model is used to store daily food wastage and has the following atributes
        1)  Date
        2)  Total food prepared
        3)  Wastage
    '''
    date = models.DateField()
    total = models.IntegerField()
    wastage = models.IntegerField()


class dish(models.Model):
    '''Model is used to store dish details and has the following atributes
        1)  Name
        2)  Price
        3)  Description
        4)  Serving time
        5)  Image
    '''
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    des = models.CharField(max_length=100)
    serve_time = models.CharField(max_length=50)
    ifile = models.ImageField(upload_to='static/assets',default='')
# Create your models here.
