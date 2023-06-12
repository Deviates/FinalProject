from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank=True,null=True
        )
    def __str__(self):
        return self.username