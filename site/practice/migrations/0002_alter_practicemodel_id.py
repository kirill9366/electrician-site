# Generated by Django 3.2.13 on 2022-05-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
