from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def homepage(request):
    return render(request, "azure_site/home.html", {})