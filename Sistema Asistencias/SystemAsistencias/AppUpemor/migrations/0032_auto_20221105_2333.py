# Generated by Django 3.2.8 on 2022-11-06 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0031_auto_20221105_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='alumno_matricula',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='directivo_id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='profesor_id',
        ),
    ]