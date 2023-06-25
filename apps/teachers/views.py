from django.shortcuts import render
from .models import Teachers
from apps.courses.models import Courses
from apps.settings.models import Setting, Anonym_messages
from apps.telegram.views import get_text 


# Create your views here.
def teachers(request):
    settings = Setting.objects.latest("id")
    teachers = Teachers.objects.all()
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")
    

    context = {
        "teachers" : teachers,
        "settings" : settings
    }

    return render(request, "basic/teachers.html", context)

def detail_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    course = Courses.objects.all()
    teachers = Teachers.objects.all()
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")

    
    return render(request, "single-teacher.html" , locals())