from django.urls import path
from .views import courses,detail_courses, buy

urlpatterns = [
    path('courses/', courses, name="courses"),
    path('detail_courses/<int:id>/', detail_courses, name="detail_courses"),
    path('buy/',buy, name="buy")
]