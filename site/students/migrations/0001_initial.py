# Generated by Django 3.1.4 on 2021-09-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students/', verbose_name='Изображение')),
                ('full_name', models.CharField(max_length=130, verbose_name='Полное имя')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Е - mail')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
