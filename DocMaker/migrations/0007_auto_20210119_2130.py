# Generated by Django 3.1.5 on 2021-01-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocMaker', '0006_auto_20210119_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiments',
            name='timestamp',
            field=models.DateTimeField(verbose_name='%Y-%m-%d'),
        ),
    ]
