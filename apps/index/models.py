from django.db import models

# Create your models here.
class Settings(models.Model):
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
