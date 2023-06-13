from django.shortcuts import render, redirect
from .models import Courses, Buy
from apps.settings.models import Setting
from apps.telegram.views import get_text

# Create your views here.
def courses(request):
    settings=Setting.objects.latest("id")
    course = Courses.objects.all()
    return render(request, "courses/index.html", locals())

def detail_courses(request,id):
    settings=Setting.objects.latest("id")
    course = Courses.objects.get(id=id)
    return render(request,'courses/detail.html',locals())

def buy(request, id):
    settings=Setting.objects.latest("id")
    course = Courses.objects.get(id=id)
    if request.method == "POST":
        buy = Buy.objects.create(user=request.user, course=course)
        return redirect('index')
    return render(request, 'courses/buy.html', locals())