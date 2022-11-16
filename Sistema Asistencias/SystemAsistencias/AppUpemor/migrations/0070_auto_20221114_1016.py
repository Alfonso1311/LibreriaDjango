# Generated by Django 3.2.8 on 2022-11-14 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUpemor', '0069_alter_directivo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumnoUser', to=settings.AUTH_USER_MODEL, verbose_name='ID_Usuario'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='status',
            field=models.CharField(default='', max_length=3, verbose_name='estatus'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profesorUser', to=settings.AUTH_USER_MODEL, verbose_name='ID_Usuario'),
        ),
    ]
