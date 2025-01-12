from django.shortcuts import render

def login(request):
    context={

    }
    return render(request, "users/login.html", context)

def registrations(request):
    context={

    }
    return render(request, "users/registrations.html", context)

def profile(request):
    context={

    }
    return render(request, "users/profile.html", context)

def logout(request):
    context={

    }
    return render(request, "users/logout.html", context)
