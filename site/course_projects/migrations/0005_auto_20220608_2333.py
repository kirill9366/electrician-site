# Generated by Django 3.2.13 on 2022-06-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_projects', '0004_auto_20220523_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='courseprojectmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
