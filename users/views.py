from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('shop:index'))
    else:
        form=UserLoginForm()
    context={
        'form':form,
    }
    return render(request, "users/login.html", context)

def registrations(request):
    if request.method=='POST':
        form=UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('shop:index'))

    else:
        form=UserRegistrationForm()

    context={
        'form':form,
    }
    return render(request, "users/registrations.html", context)

def profile(request):
    context={

    }
    return render(request, "users/profile.html", context)

def logout(request):
    auth.logout(request)
    return redirect(reverse, 'shop:index')
