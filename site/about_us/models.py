from django.db import models


class ContactInfoModel(models.Model):
    """Контактная информация"""

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='contact_info/',
    )
    email = models.EmailField(
        verbose_name='E - mail',
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=30,
        null=True,
        blank=True,
    )
    location = models.CharField(
        verbose_name='Адрес',
        max_length=255,
        null=True,
        blank=True,
    )
    vkontakte = models.CharField(
        verbose_name='Страница Вконтакте',
        max_length=255,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    def __str__(self):
        return 'Контактная информация'

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
