# Generated by Django 3.2.8 on 2022-10-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0010_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(max_length=15, primary_key=True, serialize=False)),
                ('horaEntrada', models.DateTimeField(max_length=100, verbose_name='Hora de entrada')),
            ],
        ),
    ]