from django.db import models

# Create your models here.

class Seller(models.Model) :
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    holder_name = models.CharField(max_length=25)
    ifc_code = models.CharField(max_length=25)
    bank_branch = models.CharField(max_length=25)
    account_number = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='seller/')
    
class Product(models.Model) :
    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE, default="")
    Category = models.CharField(max_length=20)
    P_Name = models.CharField(max_length=25)
    P_No = models.CharField(max_length=20)
    P_Description = models.CharField(max_length=200)
    P_Price = models.CharField(max_length=25)
    P_CurrentStock = models.CharField(max_length=25)
    p_photo = models.ImageField(upload_to='product/')
    
