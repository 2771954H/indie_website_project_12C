# Generated by Django 2.2.28 on 2024-03-12 01:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indie', '0010_game_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
