# Generated by Django 3.0.7 on 2020-07-03 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_use_purpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
    ]
