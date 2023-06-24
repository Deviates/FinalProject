from django.db import models
from apps.courses.models import Courses

# Create your models here.
class Teachers(models.Model):
    foto_teacher = models.ImageField(
        upload_to="foto_teacher/",
        verbose_name="фотография преподователя"
    )
    name_teacher = models.CharField(
        max_length=155,
        verbose_name="ФИО преподователя"
    )
    direction = models.ForeignKey(
        Courses, on_delete=models.CASCADE, 
        related_name='course'
    )
    email = models.EmailField(
        verbose_name="Почта учителя",
        null=True,blank=True
    )
    number = models.CharField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    def __str__(self):
        return self.name_teacher
    
    class Meta:
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователи"