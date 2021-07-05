from django.shortcuts import render
from products.models import ProductCategory, Product

goods = Product.objects.all()
categories = ProductCategory.objects.all()

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
