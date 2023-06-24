from django.shortcuts import render
from .models import Teachers
from apps.courses.models import Courses
from apps.settings.models import Setting


# Create your views here.
def teachers(request):
    settings = Setting.objects.latest("id")
    teachers = Teachers.objects.all()
    

    context = {
        "teachers" : teachers,
        "settings" : settings
    }

    return render(request, "basic/teachers.html", context)

def detail_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    course = Courses.objects.all()
    teachers = Teachers.objects.all()

    
    return render(request, "single-teacher.html" , locals())