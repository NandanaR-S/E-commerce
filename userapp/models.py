from django.db import models
from adminapp.models import ProductDetails


class UserModel(models.Model):
    User_id=models.AutoField(primary_key=True)  
    Username=models.CharField(max_length=255,unique=True)
    Password=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Phone_Number=models.IntegerField()
    Create_at=models.DateField(auto_now_add=True)
    Status=models.CharField(default="active",max_length=255)

class UserAddress(models.Model):
    Address_id=models.AutoField(primary_key=True)
    Address=models.CharField(max_length=255)
    Pincode=models.IntegerField()  
    User_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)


class Cart(models.Model):
    Cart_id=models.AutoField(primary_key=True)
    Product_id=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    User_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)


class OrderDetails(models.Model):
    Order_id=models.AutoField(primary_key=True)
    Product_id=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    User_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    Order_Date=models.DateField(auto_now_add=True)

class ReviewDetails(models.Model):
    Review_id=models.AutoField(primary_key=True)
    Review_Comments=models.CharField(max_length=255)
    Product_id=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    User_id=models.ForeignKey(UserModel,on_delete=models.CASCADE)


