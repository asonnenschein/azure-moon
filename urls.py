from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('azuremoon.views',
    url(r'^home/$', 'homepage'),
    url(r'^api/rest/products\.json', 'get_all_products'),
    url(r'^api/rest/collection$', 'get_collection'),
)