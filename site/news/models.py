from django.db import models


class ParagraphModel(models.Model):
    """Параграф, представляет собой блок с названием, изображением и текстом"""

    title = models.CharField(
        verbose_name='Название',
        max_length=255,
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name='Текст',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='paragraph/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.title} {self.text[:15]}'

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'


class NewsItemModel(models.Model):
    """Модель конкретной новости"""

    preview_image = models.ImageField(
        upload_to='news_item/',
    )
    preview_text = models.CharField(
        max_length=1000,
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=130,
    )
    date = models.DateField(
        verbose_name='Дата',
        auto_now=True,
    )
    content = models.ManyToManyField(
        ParagraphModel,
    )

    def __str__(self):
        return f'{self.title} {self.date}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
