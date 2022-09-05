from email.headerregistry import Address
import numbers
from socket import AddressInfo
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField("")
    experties=models.CharField(max_length=50)

class Patient(models.Model):
    name=models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile=models.IntegerField("")
    address=models.CharField(max_length=100)

class Appointment(models.Model):
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()