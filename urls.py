from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('azuremoon.views',
    url(r'^home/$', 'homepage'),
    url(r'^register/$', 'register'),
    url(r'^api/rest/products', 'get_all_products'),
    url(r'^api/rest/collection$', 'get_collection'),
    url(r'^api/rest/category$', 'get_category'),
    url(r'^api/rest/fieldValues$', 'get_values_for_field'),
    url(r'^api/rest/product$', 'get_single_product')
)