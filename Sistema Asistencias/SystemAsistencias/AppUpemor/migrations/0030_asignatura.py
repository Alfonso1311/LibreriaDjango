# Generated by Django 3.2.8 on 2022-10-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUpemor', '0029_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=100, verbose_name='Clave')),
                ('nomAsignatura', models.CharField(max_length=100, verbose_name='Nombre de Asignatura')),
                ('horario_id', models.IntegerField(verbose_name='ID_Horario')),
                ('profesor_id', models.CharField(max_length=15, verbose_name='ID_Profesor')),
                ('grupo_id', models.IntegerField(verbose_name='ID_Grupo')),
            ],
        ),
    ]
