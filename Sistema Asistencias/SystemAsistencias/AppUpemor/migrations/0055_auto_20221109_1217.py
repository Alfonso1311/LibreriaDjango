# Generated by Django 3.2.8 on 2022-11-09 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0054_grupo_alumno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='image',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='userType',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='id_alumno',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='alumnoAsis', to='AppUpemor.alumno', verbose_name='ID_Alumno'),
        ),
    ]