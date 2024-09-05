from django.db import models

class AdminModel(models.Model):
    admin_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField(max_length=255)

class CategoryDetails(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=255)


class ProductDetails(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=255)
    product_description=models.CharField(max_length=1000)
    product_price=models.IntegerField()
    category_id=models.ForeignKey(CategoryDetails,on_delete=models.CASCADE)



class Productimages(models.Model):
    product_images=models.ImageField(upload_to='Images')
    product_image_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)

