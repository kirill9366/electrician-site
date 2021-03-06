# Generated by Django 3.1.4 on 2022-06-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_exam', '0006_auto_20220608_0858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demoexamdatesmodel',
            options={'verbose_name': 'Сроки проведения', 'verbose_name_plural': 'Сроки проведения'},
        ),
        migrations.AlterModelOptions(
            name='demoexamdocmodel',
            options={'verbose_name': 'Документация', 'verbose_name_plural': 'Документация'},
        ),
        migrations.AlterModelOptions(
            name='demoexaminfomodel',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterModelOptions(
            name='demoexammontagemodel',
            options={'verbose_name': 'Монтаж', 'verbose_name_plural': 'Монтаж'},
        ),
        migrations.AlterModelOptions(
            name='demoexamprogrammodel',
            options={'verbose_name': 'Программирование', 'verbose_name_plural': 'Программирование'},
        ),
        migrations.AlterModelOptions(
            name='demoexamtroubleshootingmodel',
            options={'verbose_name': 'Поиск неисправностей', 'verbose_name_plural': 'Поиск неисправностей'},
        ),
        migrations.AlterModelOptions(
            name='resultmodel',
            options={'verbose_name': 'Лучшие результат', 'verbose_name_plural': 'Лучшие результаты'},
        ),
        migrations.AddField(
            model_name='demoexamdatesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='demoexamdocmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='demoexaminfomodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='demoexammontagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='demoexamprogrammodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='demoexamtroubleshootingmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='demoexamdatesmodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexamdatesmodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
        migrations.AlterField(
            model_name='demoexamdocmodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexamdocmodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
        migrations.AlterField(
            model_name='demoexaminfomodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexaminfomodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
        migrations.AlterField(
            model_name='demoexammontagemodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexammontagemodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
        migrations.AlterField(
            model_name='demoexamprogrammodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexamprogrammodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
        migrations.AlterField(
            model_name='demoexamtroubleshootingmodel',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexamtroubleshootingmodel',
            name='filter_num',
            field=models.IntegerField(verbose_name='Каким по счету стоит'),
        ),
    ]
