from django.db import models
from os import urandom
from binascii import b2a_hex
from django.util import timezone

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __init__(self):
        self.product_id = 'azure0' + b2a_hex(urandom(10))
        self.pub_date = timezone.now()

class Customer(model.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)