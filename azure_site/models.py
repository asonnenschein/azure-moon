from django.db import models
from os import urandom
from binascii import b2a_hex
from django.utils import timezone

# Create your models here.

#def content_file_name(instance, filename):
#    return '/'.join(['content', instance.user.username, filename])

media_path = '/Users/adrian/Documents/venv/azure_moon/azuremoon/azure_site/media'

def build_uid(this_class):
    if this_class is 'customer':
        return unicode('ac' + b2a_hex(urandom(5)))
    elif this_class is 'billing':
        return unicode('ab' + b2a_hex(urandom(5)))
    elif this_class is 'product':
        return unicode('ap' + b2a_hex(urandom(5)))

class Product(models.Model):
    '''
    Defines what constitutes a product, make sure to include a quantity*price 
    height_fieldin the UI.
    '''
    product_id = models.CharField(max_length=20, editable=True, 
        default=build_uid('product'))
    heading = models.CharField(max_length=200, default='undefined')
    subheading = models.CharField(max_length=200, default='undefined')
    description = models.TextField()
    image_1 = models.ImageField(upload_to=media_path, height_field=None, 
        width_field=None, max_length=500)
    image_2 = models.ImageField(upload_to=media_path, height_field=None, 
        width_field=None, max_length=500)
    image_3 = models.ImageField(upload_to=media_path, height_field=None, 
        width_field=None, max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=0)
    collection = models.CharField(max_length=200, default='undefined')
    category = models.CharField(max_length=200, default='undefined')
    pub_date = models.DateTimeField('date published')

    # Display name in manager application
    def __unicode__(self):
        return self.collection + ' --- ' + self.name

    # Return JSON object of all products in the database
    def all_products_serialized(self):
        json = {
            'product_id': self.product_id,
            'heading': self.name,
            'subheading': self.subheading,
            'description': self.description,
            'images': {
                'image_1': self.image_1,
                'image_2': self.image_2,
                'image_3': self.image_3
            },
            'price': self.price,
            'quantity': self.quantity,
            'collection': self.collection,
            'category': self.category,
            'pub_date': self.pub_date
        }
        return json

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