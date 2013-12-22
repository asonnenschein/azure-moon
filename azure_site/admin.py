from django.contrib import admin
from azure_site.models import Product, Customer, Billing

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Billing)