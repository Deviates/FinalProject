from django.db import models

# Create your models here.
class Setting(models.Model):
    name_site = models.CharField(
        max_length=150,
        verbose_name="Название колледжа"
    )
    logo_site = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип колледжа"
    )
    info_site = models.CharField(
        max_length=255,
        verbose_name="Дополнительная информация о колледже"
    )
    
    def __str__(self):
        return self.name_site
    
    class Meta:
        verbose_name = "Настройки колледжа"
        verbose_name_plural = "Настройки колледжа"

class Event(models.Model):
    name_event = models.CharField(
        max_length=155,
        verbose_name="Название мероприятия"
    )
    foto_event = models.ImageField(
        upload_to="event/",
        verbose_name="Фотография ивента"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    title_event = models.CharField(
        max_length=255,
        verbose_name="Заголовок мероприятия"
    )
    event_desc = models.TextField(
        max_length=255,
        verbose_name="Описасние мероприятия"
    )

    def __str__(self):
        return self.name_event
    
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    message = models.TextField(
        max_length=255,
        verbose_name="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Benefit(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание"
    )
    icon = models.ImageField(
        upload_to="icons/",
        verbose_name="Иконки",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

class About(models.Model):
    slide_1 = models.ImageField(
        upload_to="about_slide/",
        verbose_name="Фото"
    )
    info = models.CharField(
        max_length=255,
        verbose_name="О нас"
    )

    def __str__(self):
        return self.info
    
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"