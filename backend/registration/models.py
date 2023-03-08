from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    medications = models.CharField(max_length=10)
    message = models.CharField(max_length= 100)

    class Meta :
        db_table = 'register'

