from django.shortcuts import render

from apps.settings.models import Setting, Benefit
from apps.courses.models import Category, Courses
from apps.telegram.views import get_text

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')
    courses = Courses.objects.all()
    benefits = Benefit.objects.all().order_by('?')
    return render(request,'index.html',locals())