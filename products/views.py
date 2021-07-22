from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Products',
               'categories': ProductCategory.objects.all(),
               'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()}
    return render(request, 'products/products.html', context)
