from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from azuremoon.models import Product
import json

# Create your views here.

def homepage(request):
    return render(request, "azuremoon/home.html", {})

def get_products_serialized(products):
    data = [p.products_serialized() for p in products]
    return HttpResponse(json.dumps(data), content_type='application/json')

def view_all_products(products):
    return get_products_serialized(products)

def get_all_products(extension='json'):
    models = Product.objects.all()
    return view_all_products(models)

def get_collection(request):
	collection_name = request.GET.get('name')
	p = Product()
	data = p.collection_serialized(collection_name)
	return HttpResponse(json.dumps(data), content_type='application/json')

def get_category(request):
    category_name = request.GET.get('name')
    p = Product()
    data = p.category_serialized(category_name)
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_values_for_field(request):
    field_name = request.GET.get('field')
    p = Product()
    data = p.get_values_for_field(field_name)
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_single_product(request):
    product_id = request.GET.get('product_id')
    p = Product()
    data = p.get_single_product(product_id)
    return HttpResponse(json.dumps(data), content_type='application/json')