# Generated by Django 3.2.8 on 2022-10-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0004_directivo_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidoP', models.CharField(max_length=100, verbose_name='Apellido P')),
                ('apellidoM', models.CharField(max_length=100, verbose_name='Apellido M')),
                ('fechaNac', models.DateField(blank=True, null=True, verbose_name='Fecha Nac (yyyy-mm-dd)')),
                ('correo', models.EmailField(max_length=254, null=True, verbose_name='Correo')),
                ('da', models.CharField(max_length=100, null=True, verbose_name='DA')),
            ],
        ),
        migrations.AlterField(
            model_name='directivo',
            name='fechaNac',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Nac (yyyy-mm-dd)'),
        ),
    ]