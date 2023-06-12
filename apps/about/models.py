from django.db import models

# Create your models here.
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

