from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from azure_site.models import Product
import json

# Create your views here.

def homepage(request):
    return render(request, "azure_site/home.html", {})

def get_json(products):
    data = [p.serialized() for p in products]
    return HttpResponse(json.dumps(data), mimetype='application/json')

def view_products(products):
    return get_json(products)

def get_all_products(extension='json'):
    models = Product.objects.all()
    return view_products(models)