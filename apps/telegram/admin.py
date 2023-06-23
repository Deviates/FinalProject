from django.contrib import admin
from .models import TelegramUser

# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'chat_id', 'created']