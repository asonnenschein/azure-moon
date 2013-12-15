from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)