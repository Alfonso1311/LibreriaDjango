# Generated by Django 3.2.8 on 2022-10-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0027_auto_20221028_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='justificante',
            name='matricula',
            field=models.CharField(max_length=100, null=True, verbose_name='Matricula_Alumno'),
        ),
    ]