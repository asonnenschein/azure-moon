from django.contrib import admin
from azuremoon.models import Product, Variation

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['heading', 'subheading', 'description', 'price', 
			'quantity', 'collection', 'category', 'pub_date', 'on_sale']}),
		('Shipping', {'fields': ['united_states', 'australia', 
			'international']}),
		('Images', {'fields': ['image_1', 'image_2', 'image_3',
			'image_thumbnail']})
	]
	inlines = [VariationInline]
	list_display = ('heading', 'collection', 'category', 'quantity')

admin.site.register(Product, ProductAdmin)
#admin.site.register(Customer)
#admin.site.register(Billing)