# Generated by Django 3.2.8 on 2022-10-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0023_auto_20221028_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='cuatri',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellidoM',
            field=models.CharField(max_length=100, null=True, verbose_name='Apellido M'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='grupo',
            field=models.CharField(max_length=10, verbose_name='Grupo_ID'),
        ),
        migrations.AlterField(
            model_name='directivo',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='ID_Directivo'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='ID_Profesor'),
        ),
    ]
