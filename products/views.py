from django.shortcuts import render
import json


with open('products/fixtures/goods.json', 'r', encoding='utf-8') as json_file:
    goods = json.load(json_file)

# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Products',
        'products': goods
    }
    return render(request, 'products/products.html', context)
