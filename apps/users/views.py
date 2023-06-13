from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from apps.users.models import User
from apps.settings.models import Setting

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        if password == confirm_password:
            if username and password and confirm_password:
                try:
                    user = User.objects.create(username = username)
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
    return render(request, 'users/register.html', context)


def user_login(request):
    setting = Setting.objects.latest("id")
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
            return redirect('user_account', request.user.id)
        else:
            messages.error(request, 'Неправильный пароль.')
            return redirect('login')
    context = {
        "setting": setting,
    }
    return render(request, "users/login.html", context)

def user_account(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id=id)
    if request.method == "POST":
        if 'update_account' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            username = request.POST.get('username')
            profile_image = request.POST.get('profile_image')
            email = request.POST.get('email')
            bio = request.POST.get('bio')
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.username = username
            user.profile_image = profile_image
            user.email = email
            user.bio = bio
            user.save()
            return redirect('user_account', request.user.id)
    return render(request, 'users/settings.html', locals())