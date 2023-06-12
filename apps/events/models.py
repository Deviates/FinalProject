from django.db import models

# Create your models here.
class Events(models.Model):
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
