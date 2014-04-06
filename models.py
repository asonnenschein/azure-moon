from django.db import models
from django.conf import settings
from os import urandom
from binascii import b2a_hex
from django.utils import timezone

# Create your models here.

#def content_file_name(instance, filename):
#    return '/'.join(['content', instance.user.username, filename])

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
    field in the UI.
    '''

    # Individual product info
    product_id = models.CharField(max_length=20, editable=False, 
        default=build_uid('product'))
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    quantity = models.IntegerField(
        help_text='Total number of units available for sale')
    pub_date = models.DateTimeField('date published')
    on_sale = models.BooleanField(default=False)

    # Group product info
    collection = models.CharField(max_length=200, 
        help_text='Group that this product belongs to (ex: Summer Scents)')
    category = models.CharField(max_length=200, 
        help_text='Type of product (ex: Necklaces)')

    # Shipping info
    usps_fast_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    usps_average_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    usps_regular_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    other_shipping_name = models.CharField(max_length=200, 
        help_text='Name of shipping company (ex: FedEx)')
    other_fast_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    other_average_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')
    other_regular_shipping = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34')

    # Product images
    image_1 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_2 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_3 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_thumbnail = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)

    # Return JSON object of all products in the database
    def products_serialized(self):
        json = {
            'product_id': self.product_id,
            'heading': self.heading,
            'subheading': self.subheading,
            'description': self.description,
            'images': {
                'image_1': str(self.image_1),
                'image_2': str(self.image_2),
                'image_3': str(self.image_3)
            },
            'price': float(self.price),
            'quantity': self.quantity,
            'collection': self.collection,
            'category': self.category,
            'pub_date': str(self.pub_date)
        }
        return json
'''
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
    registered_user = models.BooleanField(default=False, editable=False)

class Billing(models.Model):
    billing_id = models.CharField(max_length=16, editable=False)
    num = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    sec_num = models.CharField(max_length=200)
'''