from django.shortcuts import render
from .models import Teachers
from apps.courses.models import Courses
from apps.index.models import Settings
from apps.telegram.views import get_text
from apps.contacts.models import  Anonym_messages


# Create your views here.
def teachers(request):
    settings = Settings.objects.latest("id")
    teachers = Teachers.objects.all()
    

    context = {
        "teachers" : teachers,
        "settings" : settings
    }

    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")

    return render(request, "teachers.html", context)

def detail_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    course = Courses.objects.all()
    teachers = Teachers.objects.all()

    
    return render(request, "single-teacher.html" , locals())