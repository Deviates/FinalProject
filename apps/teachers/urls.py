from django.urls import path
from .views import teachers, detail_teacher

urlpatterns = [
    path("teachers/", teachers, name="teachers"),
    path('detail_teacher/<int:id>/', detail_teacher, name="detail_teacher")
]