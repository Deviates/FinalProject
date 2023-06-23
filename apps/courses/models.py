from django.db import models

from apps.users.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="Slug"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Courses(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="category_courses",
        null=True, verbose_name="Категория"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название курса"
    )
    image = models.ImageField(
        upload_to="product/",
        verbose_name="Фотография продукта"
    )
    price = models.BigIntegerField(
        verbose_name="Цена курса"
    )
    description = models.TextField(
        verbose_name="Описание продукта"       
    )
    duration = models.CharField(
        max_length=100,
        verbose_name="Длительность"
    )
    url = models.URLField(
        verbose_name="Ссылка на курс"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наши курсы"
        verbose_name_plural = "Наши курсы"

class Buy(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="users_buys",
        verbose_name="Пользователь"
    )
    course = models.ForeignKey(
        Courses, on_delete=models.SET_NULL,
        related_name="buys_courses",
        verbose_name="Курсы",
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата покупки"
    )

    def __str__(self):
        return f"{self.user} {self.course}"

    class Meta:
        verbose_name = "купить курс"
        verbose_name_plural = "купить курсы"