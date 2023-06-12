# Generated by Django 4.2 on 2023-06-05 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_teacher', models.ImageField(upload_to='foto_teacher/', verbose_name='фотография преподователя')),
                ('name_teacher', models.CharField(max_length=155, verbose_name='ФИО преподователя')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.courses')),
            ],
            options={
                'verbose_name': 'Преподователь',
                'verbose_name_plural': 'Преподователи',
            },
        ),
    ]
