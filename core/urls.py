"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from apps.index import urls
from apps.about import urls
from apps.contacts import urls
from apps.courses import urls
from apps.events import urls
from apps.teachers import urls
from apps.users import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('', include("apps.about.urls")),
    path('', include("apps.contacts.urls")),
    path('', include("apps.courses.urls")),
    path('', include("apps.events.urls")),
    path('', include("apps.teachers.urls")),
    path('', include("apps.users.urls")),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)