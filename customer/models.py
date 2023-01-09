from django.db import models


# Create your models here.

class Customer(models.Model) :
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

    
