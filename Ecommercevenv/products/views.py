from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_product = Product.objects.order_by('-priority')[:4]
    latest_product = Product.objects.order_by('-id')[:4]
    context = {
        'featured_product' : featured_product,
        'latest_product' : latest_product,
    }
    return render(request,'index.html',context)

def products_list(request):
    product = Product.objects.order_by('priority')
    product_paginator = Paginator(product,4)
    page = request.GET.get('page')
    product = product_paginator.get_page(page)
    context = {
        'product' : product
    }
    return render(request,'products.html',context)

def detail_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request,'product_details.html',context)