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

    class Meta:
        verbose_name = "Лучшие результат"
        verbose_name_plural = "Лучшие результаты"


class DemoExamInfoModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"


class DemoExamDocModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Документация"
        verbose_name_plural = "Документация"


class DemoExamDatesModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Сроки проведения"
        verbose_name_plural = "Сроки проведения"


class DemoExamMontageModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Монтаж"
        verbose_name_plural = "Монтаж"


class DemoExamProgramModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Программирование"
        verbose_name_plural = "Программирование"


class DemoExamTroubleShootingModel(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        null=True,
        blank=True,
    )
    content = models.TextField(
        verbose_name="Контент",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    filter_num = models.IntegerField(
        verbose_name="Каким по счету стоит",
    )

    class Meta:
        verbose_name = "Поиск неисправностей"
        verbose_name_plural = "Поиск неисправностей"
