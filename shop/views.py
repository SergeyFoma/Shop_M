from django.shortcuts import render
from goods.models import Categorys, Products

def index(request):
    #good=get_object_or_404(Categorys, slug=category_slug)
    #good=Categorys.objects.all()
    context={
        "title": "Houme page",
        #'good':good,
    }
    return render(request,"shop/index.html",context)

def about(request):
    
    context={
        'title':'about',
        
    }
    return render(request, "shop/about.html", context)


