from django.urls import path
from django.contrib.auth.views import LogoutView  
from .views import register, us_login
# from .views import
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", us_login, name="login"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
]