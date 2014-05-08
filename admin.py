from django.contrib import admin
from azuremoon.models import Product, Variation, Shipping, UserProfile

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['heading', 'subheading', 'description', 'price', 
			'quantity', 'collection', 'category', 'pub_date', 'on_sale']}),
		('Images', {'fields': ['image_1', 'image_2', 'image_3',
			'image_thumbnail']})
	]
	inlines = [VariationInline]
	list_display = ('heading', 'collection', 'category', 'quantity')

class ShippingAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['place', 'price']})
	]
	list_display = ('place', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(UserProfile)
#admin.site.register(Billing)