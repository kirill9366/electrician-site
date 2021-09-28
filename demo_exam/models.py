from django.db import models


class ResultModel(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='result/',
    )
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=255,
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='E - mail',
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=224,
    )
