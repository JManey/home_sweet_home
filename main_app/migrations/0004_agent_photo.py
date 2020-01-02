# Generated by Django 3.0 on 2020-01-02 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile')),
            ],
        ),
    ]
