from django.db import models

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

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наши курсы"
        verbose_name_plural = "Наши курсы"

class Buy(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    buy_course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        related_name="buy_courses"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "купить курс"
        verbose_name_plural = "купить курсы"