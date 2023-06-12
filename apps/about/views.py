from django.shortcuts import render
from apps.contacts.models import  Anonym_messages
from apps.telegram.views import get_text
from . models import About
from apps.index.models import Settings

# Create your views here.
def about(request):
    settings = Settings.objects.latest("id")
    about = About.objects.all()
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")
    context = {
        'about' : about,
        "settings" : settings
    }
    return render(request,'about.html',context)

