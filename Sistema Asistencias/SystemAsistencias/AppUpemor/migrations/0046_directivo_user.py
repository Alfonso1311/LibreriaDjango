# Generated by Django 3.2.8 on 2022-11-06 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUpemor', '0045_alter_usuario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='directivo',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='directivo', to=settings.AUTH_USER_MODEL),
        ),
    ]
