from django.db import models

# Create your models here.
class Contacts(models.Model):
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