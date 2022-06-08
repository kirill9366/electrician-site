# Generated by Django 3.1.4 on 2021-09-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseprojectmodel',
            name='file',
            field=models.FileField(default=None, upload_to='course_projects/', verbose_name='Файл'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseprojectmodel',
            name='image',
            field=models.ImageField(upload_to='course_projects/', verbose_name='Изображение'),
        ),
    ]
