# Generated by Django 3.2.13 on 2022-06-08 23:33

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo_exam', '0007_auto_20220608_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='demoexaminfomodel',
            name='_content_rendered',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='demoexamdatesmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='demoexamdocmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='demoexaminfomodel',
            name='content',
            field=precise_bbcode.fields.BBCodeTextField(blank=True, no_rendered_field=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='demoexaminfomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='demoexammontagemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='demoexamprogrammodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='demoexamtroubleshootingmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='resultmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
