from django.urls import path
from django.contrib.auth.views import LogoutView  
from apps.users.views import register, user_login, user_account, my_ajax_view


urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('user/<int:id>/', user_account, name="user_account"),
    path('my-ajax-view/', my_ajax_view, name='my-ajax-view'),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
]