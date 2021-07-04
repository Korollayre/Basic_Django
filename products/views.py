from django.shortcuts import render
import json


with open('products/fixtures/goods.json', 'r') as json_file:
    goods = json.load(json_file)

with open('products/fixtures/categories.json', 'r') as json_file:
    categories = json.load(json_file)

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Products',
        'products': goods,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)
