# Generated by Django 3.2.8 on 2022-11-10 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0058_auto_20221109_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='carrera',
        ),
    ]
