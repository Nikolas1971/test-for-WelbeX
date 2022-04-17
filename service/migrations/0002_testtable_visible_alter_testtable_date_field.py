# Generated by Django 4.0.4 on 2022-04-17 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='testtable',
            name='date_field',
            field=models.DateField(default=datetime.date(2022, 4, 17), verbose_name='Дата'),
        ),
    ]
