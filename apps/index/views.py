from django.shortcuts import render
from .models import Settings
from apps.courses.models import Courses
from apps.contacts.models import  Anonym_messages
from apps.telegram.views import get_text

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    cource = Courses.objects.all()
    context ={
        'settings':settings,
        "cource" : cource
    }
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")
    return render(request,'index.html',context)