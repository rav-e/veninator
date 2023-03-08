from django.db import models

# Create your models here.

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default=None)
    email = models.EmailField(max_length=100,default=None)
    location = models.CharField(max_length=100,default=None)
    date = models.DateField(max_length=50,default=None)
    vaccine = models.CharField(max_length=50,default=None)
    time = models.TimeField(max_length= 5,default=None)

    class Meta:
        db_table = 'appointment'
