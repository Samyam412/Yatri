from django.db import models

# Create your models here.
from email.policy import default
from itertools import product
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(ProductCategory,null=True,blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    inStock = models.BooleanField()
    image = models.ImageField(default='default.jpg',upload_to='productImage',null=True,blank=True)


    def __str__(self):
        return f'{self.name}'

class freshSale(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'