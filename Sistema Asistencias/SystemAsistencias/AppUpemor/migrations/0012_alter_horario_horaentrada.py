# Generated by Django 3.2.8 on 2022-10-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0011_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horaEntrada',
            field=models.DateTimeField(verbose_name='Hora de entrada'),
        ),
    ]
