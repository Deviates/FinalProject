from django.urls import path
from .views import courses,detail_courses, buy

urlpatterns = [
    path('', courses, name="courses"),
    path('<int:id>/', detail_courses, name="detail_courses"),
    path('buy/<int:id>/',buy, name="buy")
]