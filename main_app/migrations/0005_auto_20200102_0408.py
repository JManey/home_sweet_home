# Generated by Django 3.0 on 2020-01-02 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_agent_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_photo',
            name='profile',
        ),
        migrations.AddField(
            model_name='agent_photo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
