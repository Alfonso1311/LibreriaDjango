# Generated by Django 3.2.8 on 2022-09-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0002_auto_20220930_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directivo',
            name='fechaNac',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Nac'),
        ),
    ]
