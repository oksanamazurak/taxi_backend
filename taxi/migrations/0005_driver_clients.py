# Generated by Django 3.2.23 on 2023-12-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_remove_driver_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='clients',
            field=models.ManyToManyField(related_name='orders', through='taxi.Order', to='taxi.Client'),
        ),
    ]
