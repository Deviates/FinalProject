from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.settings.models import Setting, Benefit,Contact,About,Data
from apps.courses.models import Category, Courses
from apps.telegram.views import get_text

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')
    courses = Courses.objects.all()
    benefits = Benefit.objects.all().order_by('?')
    return render(request,'basic/index.html',locals())

def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    data = Data.objects.latest('id')
    return render(request,'basic/about.html',locals())

def contacts(request):
    setting = Setting.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',

            f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся.Ваще сообщение: {message} Ваша почта: {email}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
    return render(request,'basic/contacts.html',locals())