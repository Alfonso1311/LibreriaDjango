# Generated by Django 3.2.8 on 2022-10-08 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0008_alumno_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='foto',
        ),
    ]
