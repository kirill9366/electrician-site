from django.db import models


class StudentModel(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='students/',
    )
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=130,
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='Е - mail',
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
