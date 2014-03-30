from django.contrib import admin
from azure_site.models import Product, Customer, Billing

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['heading', 'subheading', 'description', 'price', 
			'quantity', 'collection', 'category', 'pub_date', 'on_sale']}),
		('Images', {'fields': ['image_1', 'image_2', 'image_3']})
	]
	list_display = ('heading', 'collection', 'category', 'quantity')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Billing)