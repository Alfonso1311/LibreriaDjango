# Generated by Django 3.2.8 on 2022-10-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0022_auto_20221028_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directivo',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ID_Directivo'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellidoM',
            field=models.CharField(max_length=100, null=True, verbose_name='Apellido M'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ID_Profesor'),
        ),
    ]
