# Generated by Django 3.2.8 on 2022-09-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0003_alter_directivo_fechanac'),
    ]

    operations = [
        migrations.AddField(
            model_name='directivo',
            name='area',
            field=models.CharField(max_length=100, null=True, verbose_name='Area'),
        ),
    ]
