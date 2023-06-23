from django.shortcuts import render, redirect
from apps.courses.models import Courses, Buy
from apps.settings.models import Setting
from apps.telegram.views import get_text

# Create your views here.
def courses(request):
    setting=Setting.objects.latest("id")
    course = Courses.objects.all()
    return render(request, "courses/index.html", locals())

def detail_courses(request,id):
    setting=Setting.objects.latest("id")
    course = Courses.objects.get(id=id)
    user_course = Buy.objects.filter(user=request.user.id, course=course.id)

    return render(request,'courses/detail.html',locals())

def buy(request, id):
    course = Courses.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        user.balance -= course.price
        user.save()
        purchase = Buy(course=course, user=user)
        purchase.save()
        return redirect('/')
    return render(request, 'courses/buy.html', {'course': course})