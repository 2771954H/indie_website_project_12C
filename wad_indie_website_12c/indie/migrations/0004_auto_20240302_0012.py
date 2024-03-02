# Generated by Django 2.2.28 on 2024-03-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indie', '0003_auto_20240301_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.CharField(default=None, max_length=9999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='downloads',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
