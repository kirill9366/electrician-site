# Generated by Django 3.1.4 on 2022-05-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_addinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
