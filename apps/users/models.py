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
    referral_code = models.CharField(
        max_length=20, 
        verbose_name="Реферальный код"
    )
    bonus = models.CharField(
        max_length=10,
        verbose_name="Бонусный код",
        blank=True, null=True
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
    
    @staticmethod
    def generate_referral_code():   
        characters = string.ascii_letters + string.digits
        ref_code = ''.join(random.choice(characters) for _ in range(10)).upper()
        return ref_code
    
    def save(self, *args, **kwargs):
        if not self.referral_code and not self.wallet_id:
            self.referral_code = self.generate_referral_code()
            self.wallet_id = self.generate_wallet_id()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    
class MoneyTransfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_user', verbose_name='Отправитель')
    wallet_address = models.CharField(max_length=50, verbose_name="Адрес кошелька")
    amount = models.PositiveIntegerField(verbose_name='Сумма перевода')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "Перевод денег"
        verbose_name_plural = "Переводы денег"