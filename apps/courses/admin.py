from django.contrib import admin
from .models import Category, Courses, Buy

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(Courses)
admin.site.register(Buy)