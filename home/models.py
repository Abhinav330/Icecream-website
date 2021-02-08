from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    desc=models.TextField()
    date=models.DateField()

class Booking(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    desc=models.TextField()
    date=models.DateField()

