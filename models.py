from django.db import models
from django.conf import settings
from os import urandom
from binascii import b2a_hex
from django.utils import timezone

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
    heading = models.CharField(max_length=200, blank=True)
    subheading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34', blank=True)
    quantity = models.IntegerField(
        help_text='Total number of units available for sale', blank=True)
    pub_date = models.DateTimeField('date published', blank=True)
    on_sale = models.BooleanField(default=False, blank=True)

    # Group product info
    collection = models.CharField(max_length=200, blank=True,
        help_text='Group that this product belongs to (ex: Summer Scents)')
    category = models.CharField(max_length=200, blank=True, 
        help_text='Type of product (ex: Necklaces)')

    # Product images
    image_1 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_2 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_3 = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)
    image_thumbnail = models.ImageField(upload_to=settings.MEDIA_ROOT, 
        height_field=None, width_field=None, max_length=500, blank=True)

    def get_variations(self, id):
        try:
            product_variations = []
            variations = Variation.objects.filter(product_id=id)
            for v in variations:
                select = {
                    'variation': v.variation,
                    'price': float(v.price)
                }
                product_variations.append(select)
            return product_variations
        except:
            return "Undefined"

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
            'pub_date': str(self.pub_date),
            'variations': self.get_variations(self.pk)
        }
        return json

    def filter_collection(self, collection_name):
        if self.collection is None:
            return Product.objects.none()
        return Product.objects.filter(collection=collection_name)

    def filter_category(self, category_name):
        if self.category is None:
            return Product.objects.none()
        return Product.objects.filter(category=category_name)

    def selection_serialized(self, function, query):
        matched_resources = []
        matches = function(query)
        for match in matches:
            json = {
                'product_id': match.product_id,
                'heading': match.heading,
                'subheading': match.subheading,
                'description': match.description,
                'images': {
                    'image_1': str(match.image_1),
                    'image_2': str(match.image_2),
                    'image_3': str(match.image_3)
                },
                'price': float(match.price),
                'quantity': match.quantity,
                'collection': match.collection,
                'category': match.category,
                'pub_date': str(match.pub_date),
                'variations': match.get_variations(match.pk)
            }
            matched_resources.append(json)
        return matched_resources

    def collection_serialized(self, query):
        do_filter = self.filter_collection
        return self.selection_serialized(do_filter, query)

    def category_serialized(self, query):
        do_filter = self.filter_category
        return self.selection_serialized(do_filter, query)


class Variation(models.Model):
    '''
    Products can have different types, like blue or green.  Foreign 
    relationship to Products model.  Make this a tabular inline form.
    '''
    product = models.ForeignKey(Product)
    variation = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34', blank=True)

class Shipping(models.Model):
    '''
    Flat shipping rates for different locations.
    '''
    # Shipping Info
    place = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, 
        help_text='Please use this format: 12.34', blank=True)