from django.db import models
from os import urandom
from binascii import b2a_hex
from django.utils import timezone

# Create your models here.

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class Product(models.Model):
    product_id = models.CharField(max_length=16, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to=content_file_name, height_field=None, width_field=None, max_length=100)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __init__(self):
        self.product_id = 'azure0' + b2a_hex(urandom(10))
        self.pub_date = timezone.now()

class Customer(models.Model):
    customer_id = models.CharField(max_length=16, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)

    def __init__(self):
        self.product_id = 'azure0' + b2a_hex(urandom(10))
        self.pub_date = timezone.now()

class Billing(models.Model):
    billing_id = models.CharField(max_length=16, editable=False)
    num = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    sec_num = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __init__(self):
        self.product_id = 'azure0' + b2a_hex(urandom(10))
        self.pub_date = timezone.now()