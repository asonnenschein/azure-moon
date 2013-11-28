from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^azure_site/', include('azure_site.urls', namespace='azure_site')),
    url(r'^admin/', include(admin.site.urls)),
)
