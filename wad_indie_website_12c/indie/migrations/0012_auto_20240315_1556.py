# Generated by Django 2.2.28 on 2024-03-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indie', '0011_auto_20240312_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Platformer', 'Platformer'), ('Puzzle', 'Puzzle'), ('RPG', 'RPG')], max_length=128, unique=True),
        ),
    ]
