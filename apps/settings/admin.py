from django.contrib import admin

from apps.settings.models import Setting, Contact, Event, About, Benefit

# Register your models here.
@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name_site', 'info_site', 'logo_site']

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
