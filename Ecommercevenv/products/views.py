from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

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
    query = request.GET.get('q')
    category = request.GET.get('category')
    product_list = Product.objects.filter(delete_status=Product.LIVE).order_by('priority')

    if query:
        product_list = product_list.filter(Q(title__icontains=query))

    if category:
        product_list = product_list.filter(Category__title=category)

    product_paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    products = product_paginator.get_page(page)
    categories = Category.objects.all()
     
    context = {
        'product': products,
        'search_query': query,
        'categories': categories
    }
    return render(request, 'products.html', context)

def detail_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request,'product_details.html',context)