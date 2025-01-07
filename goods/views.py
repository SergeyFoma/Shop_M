from django.shortcuts import render, get_object_or_404, get_list_or_404
from goods.models import Categorys, Products
from django.core.paginator import Paginator
from goods.utils import q_search

def catalog(request, category_slug=None):
    page=request.GET.get('page', 1)
    on_sale=request.GET.get('on_sale', None)
    order_by=request.GET.get('order_by', None)
    query=request.GET.get('q', None)

    if category_slug == 'all':
        good=Products.objects.all()
    elif query: #прописано в utils.py
        good=q_search(query)
    else:
        good=Products.objects.filter(category__slug=category_slug)

    if on_sale:
        good=good.filter(discount__gt=0)

    if order_by and order_by != 'default':
        good=good.order_by(order_by)

    paginator=Paginator(good, 3)
    #page_number=request.GET.get('page')
    #page_obj=paginator.get_page(page_number)    
    current_page=paginator.page(int(page))
    context={
        #'page_obj':page_obj,
        'good':current_page,
        'category_slug':category_slug,
    }
    return render(request, "goods/catalog.html", context)

def products(request, prod_slug=None):
    prod=get_object_or_404(Products, slug=prod_slug)
    context={
        'prod':prod,
    }
    return render(request, "goods/products.html", context)


