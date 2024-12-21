from django.shortcuts import render
from goods.models import Categorys, Products
from django.core.paginator import Paginator

def catalog(request):
    categorys=Categorys.objects.all()
    prod=Products.objects.all()

    paginator=Paginator(prod, 3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'title': 'catalog',
        'categorys':categorys,
        "prod":prod,
        'page_obj':page_obj,
    }
    return render(request, "goods/catalog.html", context)

def products(request):
    
    context={
        "title":"products",
        
    }
    return render(request, "goods/products.html", context)

