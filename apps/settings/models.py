from django.db import models

# Create your models here.
class Setting(models.Model):
    name_site = models.CharField(
        max_length=150,
        verbose_name="Название сайта"
    )
    logo_site = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    info_site = models.CharField(
        max_length=255,
        verbose_name="Дополнительная информация о сайте"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон номер',
        blank=True, null=True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True, null=True
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.name_site
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"

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
    image = models.ImageField(
        upload_to="about_slide/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"
        
class Data(models.Model):
    online_course = models.CharField(
        max_length=255,
        verbose_name="Онлайн курсов"
    )
    active_students = models.CharField(
        max_length=255,
        verbose_name="Активных студентов"
    )
    expert_instructor = models.CharField(
        max_length=255,
        verbose_name="Экспертных инструкторов"
    )
    hours_educate = models.CharField(
        max_length=255,
        verbose_name="Часов обучения"
    )
    def __str__(self):
        return self.online_course
    
    class Meta:
        verbose_name="Мы в числах"
        verbose_name_plural="Мы в числах"

class Anonym_messages(models.Model):
    name2 = models.CharField(
        max_length=155,
        verbose_name="кому"
    )
    message2 = models.TextField(
        max_length=255,
        verbose_name="Введите ваше сообщение"
    )
    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = "Анонимное сообщение"
        verbose_name_plural = "Анонимные сообщения"