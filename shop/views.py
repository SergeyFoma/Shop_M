from django.shortcuts import render

def index(request):
    context={
        "title": "Houme page",
    }
    return render(request,"shop/index.html",context)

def about(request):
    context={
        'title':'about',
    }
    return render(request, "shop/about.html", context)

def products(request):
    context={
        'title':'products',
    }
    return render(request, "shop/products.html", context)
