# Generated by Django 3.2.7 on 2021-09-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
