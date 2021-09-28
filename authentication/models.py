from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class AddInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    full_name = models.CharField(
        verbose_name='Полноя имя',
        max_length=255,
    )
    course_num = models.IntegerField(
        verbose_name='Курс',
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1),
        ]
    )

    def __str__(self):
        return f'{self.user}: {self.balance}'


@receiver(post_save, sender=User)
def subscribe_page_post_save(sender, created, instance, **kwargs):
    if created:
        AddInfo.objects.create(user=instance)
