# Generated by Django 3.0 on 2019-12-20 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_property'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='listing_agent',
            new_name='user',
        ),
    ]
