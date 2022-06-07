from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
    )
    page = models.CharField(
        max_length=2,
        choices=[
            ("lb", "Библиотека"),
            ("dm", "Демо - экзамен"),
        ],
        verbose_name="Для страницы",
    )


class BookModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
    )
    file = models.FileField(
        verbose_name="Файл книги",
        upload_to="books/",
    )
    category = models.ForeignKey(
        CategoryModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="books"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
