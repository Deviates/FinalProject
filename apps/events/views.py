from django.shortcuts import render
from .models import Events
from apps.telegram.views import get_text
from apps.contacts.models import Anonym_messages
# Create your views here.

def events(request):
    events = Events.objects.all()
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")

    context = {
        "events" : events
    }
    return render(request, "events.html", context)