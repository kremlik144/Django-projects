# Generated by Django 4.2.6 on 2023-11-06 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 13, 26, 5, 108063)),
        ),
    ]
