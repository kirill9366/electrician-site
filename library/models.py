from django.db import models


class BookModel(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    file = models.FileField(
        verbose_name='Файл книги',
        upload_to='books/',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
