# Generated by Django 4.2.1 on 2023-07-31 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorystockmodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2023, 7, 31)),
        ),
        migrations.AlterField(
            model_name='inventorystockoutmodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2023, 7, 31)),
        ),
        migrations.AlterField(
            model_name='inventorystockoutsummarymodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2023, 7, 31)),
        ),
    ]
