from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile_images/",
        verbose_name="Фотография"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank=True,null=True
    )
    balance = models.PositiveBigIntegerField(
        verbose_name="Баланс",
        default=0
    )
    bio = models.TextField(
        verbose_name="BIO",
        blank=True, null=True
    )
    wallet_id = models.CharField(
        max_length=20,
        verbose_name="ID счета"
    )

    def save(self, *args, **kwargs):
        if not self.wallet_id:
            self.wallet_id = self.generate_wallet_id()
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_wallet_id():
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(20)).lower()
        return code

    def __str__(self):
        return self.username