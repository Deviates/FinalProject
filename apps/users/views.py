from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.contrib import messages
from .models import User
from apps.index.models import Settings

# Create your views here.
def register(request):
    setting = Settings.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('events')
            else:
                return redirect('events')
        else:
            return redirect('events')
    context = {
        'setting' : setting,
    }
    return render(request, 'register.html', context)


def us_login(request):
    setting = Settings.objects.latest("id")
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неправильный пароль.')
            return redirect('login')
    context = {
        "setting": setting,
    }
    return render(request, "login.html", context)