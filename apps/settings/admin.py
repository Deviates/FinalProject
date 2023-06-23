from django.contrib import admin

from apps.settings.models import Setting, Contact, Event, About, Benefit,Data

# Register your models here.
@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name_site', 'info_site', 'logo_site']

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('online_course', 'active_students', 'expert_instructor','hours_educate')