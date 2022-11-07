# Generated by Django 3.2.8 on 2022-11-06 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUpemor', '0044_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]