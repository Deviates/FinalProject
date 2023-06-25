from django.shortcuts import render, redirect

from apps.courses.models import Courses, Buy
from apps.settings.models import Setting, Anonym_messages
from apps.telegram.views import get_text

# Create your views here.
def courses(request):
    setting=Setting.objects.latest("id")
    course = Courses.objects.all()
    if request.method == "POST":
        name2 = request.POST.get("name2")
        message2 = request.POST.get("message2")

        reviews = Anonym_messages.objects.create(name2 = name2, message2 = message2)

        get_text(f""" Оставлен анонимный отзыв
Кому: {reviews.name2}
Текст: {reviews.message2}
""")
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
        if user.balance >= course.price:
            user.balance -= course.price
            user.save()
            purchase = Buy(course=course, user=user)
            purchase.save()
            return redirect('/')
        else:
            return render(request, 'courses/error_page.html')
    return render(request, 'courses/buy.html', {'course': course})