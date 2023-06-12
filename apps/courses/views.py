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

def buy(request):
    settings=Setting.objects.latest("id")
    courses=Courses.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get('course')
        
        review = Buy.objects.create(name = name, email = email, phone = phone, buy_course_id = int(course))

        get_text(f"""Заявка на покупку:
Пользователь {review.name} хочет купить курс по {review.buy_course}
Его email {review.email},
Номер телеофона {review.phone}
""")
        return redirect("index")
        
    context ={
        'settings':settings,
        'courses' : courses
    }
    return render(request, 'forma.html', context)