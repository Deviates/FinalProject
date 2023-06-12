from django.shortcuts import render,redirect
from .models import Contacts
from apps.index.models import Settings
from apps.telegram.views import get_text

# Create your views here.
def contacts(request):
    settings =  Settings.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        review = Contacts.objects.create(name = name, email = email, message = message)

        get_text(f""" Оставлен отзыв 
Имя пользователя: {review.name}
Адрес(email): {review.email}
Текст: {review.message}
""")

        return redirect("index")


    context ={
        'settings':settings
    }
    return render(request, 'contacts.html',context)