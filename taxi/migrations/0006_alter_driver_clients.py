# Generated by Django 3.2.23 on 2023-12-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0005_driver_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='clients',
            field=models.ManyToManyField(through='taxi.Order', to='taxi.Client'),
        ),
    ]
