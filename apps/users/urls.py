from django.urls import path
from django.contrib.auth.views import LogoutView  
from apps.users.views import register, user_login


urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
]