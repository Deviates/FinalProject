# Generated by Django 4.2 on 2023-06-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта учителя'),
        ),
    ]