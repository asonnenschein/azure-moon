from django.conf.urls import patterns, url
from django.conf import settings
from azure_site import views

urlpatterns = patterns('',
    url(r'^home/$', views.homepage, name='homepage')
)