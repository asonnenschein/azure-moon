from django.contrib import admin
from azuremoon.models import Product

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['heading', 'subheading', 'description', 'price', 
			'quantity', 'collection', 'category', 'pub_date', 'on_sale']}),
		('USPS Shipping', {'fields': ['usps_fast_shipping', 
			'usps_average_shipping', 'usps_regular_shipping']}),
		('Other Shipping', {'fields': ['other_fast_shipping', 
			'other_average_shipping', 'other_regular_shipping']}),
		('Images', {'fields': ['image_1', 'image_2', 'image_3',
			'image_thumbnail']})
	]
	list_display = ('heading', 'collection', 'category', 'quantity')

admin.site.register(Product, ProductAdmin)
#admin.site.register(Customer)
#admin.site.register(Billing)