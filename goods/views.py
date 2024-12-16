from django.shortcuts import render

def catalog(request):
    context={
        'title': 'catalog',
    }
    return render(request, "goods/catalog.html", context)

def products(request):
    context={
        "title":"products"
    }
    return render(request, "goods/products.html", context)

