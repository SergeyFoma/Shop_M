from django.shortcuts import render

def index(request):
    context={
        "title": "Houme page",
    }
    return render(request,"shop/index.html",context)
