from django.contrib import admin
from .models import Contacts, Anonym_messages

# Register your models here.
admin.site.register(Contacts)
admin.site.register(Anonym_messages)