from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Products_Collection(models.Model):
    image=models.ImageField(upload_to='images')
    vendor=models.CharField(max_length=100)
    product_title=models.CharField(max_length=100)
    rating=models.FloatField()
    price=models.FloatField()
    desc=models.TextField(max_length=500,blank=True)
    weight_in_gm = models.IntegerField(null=True,blank=True)
    aroma=models.CharField(max_length=100,blank=True)
    appearance=models.CharField(max_length=100,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    type=models.CharField(max_length=100,blank=True)
    product_slug=AutoSlugField(populate_from="product_title",unique=True,null=True,default=None)
    
    def __str__(self):
        return self.product_title

# class User_Product(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False,blank=True,null=True)
#     product
class Cart(models.Model):
    name=models.CharField(max_length=100,default="admin",unique=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Carts(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False) 
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,db_constraint=False,related_name="items",null=True)
    product=models.ForeignKey(Products_Collection,on_delete=models.CASCADE,db_constraint=False)
    quantity=models.PositiveIntegerField() 

    def __str__(self):
        return self.product.product_title


