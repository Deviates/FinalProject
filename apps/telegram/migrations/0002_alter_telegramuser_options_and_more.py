# Generated by Django 4.2 on 2023-06-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramuser',
            options={'verbose_name': 'Пользователь телеграм', 'verbose_name_plural': 'Пользователи телеграма'},
        ),
        migrations.RemoveField(
            model_name='telegramuser',
            name='id_telegram',
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='chat_id',
            field=models.CharField(default=1, max_length=100, verbose_name='Чат ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='id_user',
            field=models.CharField(default=1, max_length=100, verbose_name='ID пользователя telegram'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя пользователя'),
        ),
    ]
