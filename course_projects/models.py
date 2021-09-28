from django.db import models

# locale imports
from news.models import ParagraphModel


class CourseModel(models.Model):
    number = models.IntegerField(
        verbose_name='Номер',
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class CourseProjectModel(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='course_projects/',
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=26,
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=255,
    )
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        null=True,
        blank=True,
    )
    content = models.ManyToManyField(
        ParagraphModel,
        verbose_name='Контент',
    )
    file = models.FileField(
        verbose_name='Файл',
        upload_to='course_projects/',
    )

    def __str__(self):
        return f'{self.title} {self.subtitle[:15]}'

    class Meta:
        verbose_name = 'Курсовой проект'
        verbose_name_plural = 'Курсовые проекты'
