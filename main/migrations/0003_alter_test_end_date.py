# Generated by Django 5.0 on 2024-01-01 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 5, 3, 25, 625176, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
    ]
