from django.db import models
from os import urandom
from binascii import b2a_hex
from django.utils import timezone

# Create your models here.

#def content_file_name(instance, filename):
#    return '/'.join(['content', instance.user.username, filename])

file = '/Users/adrian/Documents/venv/azure_moon/azuremoon/azure_site/media'

class Product(models.Model):
    product_id = models.CharField(max_length=16, editable=False, default='undefined')
    name = models.CharField(max_length=200, default='undefined')
    collection = models.CharField(max_length=200, default='undefined')
    description_head = models.CharField(max_length=200, default='undefined')
    description_body = models.CharField(max_length=10000, default='undefined')
    description_extras = models.CharField(max_length=200, default='undefined')
    description_comes_with = models.CharField(max_length=200, default='undefined')
    overview = models.CharField(max_length=1000, default='undefined')
    material = models.CharField(max_length=200, default='undefined')
    handmade = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default='undefined')
    image_1 = models.ImageField(upload_to=file, height_field=None, width_field=None, max_length=500, default='undefined')
    image_2 = models.ImageField(upload_to=file, height_field=None, width_field=None, max_length=500, default='undefined')
    image_3 = models.ImageField(upload_to=file, height_field=None, width_field=None, max_length=500, default='undefined')
    image_thumb = models.ImageField(upload_to=file, height_field=None, width_field=None, max_length=500, default='undefined')
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return unicode('azure0' + b2a_hex(urandom(10)))
#        self.pub_date = timezone.now()

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