from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт.")

                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET.get('next'))
                    
                return HttpResponseRedirect(reverse('users:profile'))
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
            messages.success(request, f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт.")
            return HttpResponseRedirect(reverse('shop:index'))

    else:
        form=UserRegistrationForm()

    context={
        'form':form,
    }
    return render(request, "users/registrations.html", context)

@login_required #закрываем доступ для неавторизованных пользователей
def profile(request):
    if request.method == 'POST':
        form=ProfileForm(data=request.POST, instance=request.user, files=request.Files)
        if form.is_valid():
            form.save()
            messages.success(request, f"{username}, профайл успешно обновлен")
            return redirect(reverse('users:profile'))
    else:
        form=ProfileForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта.")
    auth.logout(request)
    return redirect(reverse('shop:index'))
