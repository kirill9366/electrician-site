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


class DemoExamInfoModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()


class DemoExamDocModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()


class DemoExamDatesModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()


class DemoExamMontageModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()


class DemoExamProgramModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()


class DemoExamTroubleShootingModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField()
