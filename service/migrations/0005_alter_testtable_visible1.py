# Generated by Django 4.0.4 on 2022-04-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_testtable_visible1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtable',
            name='visible1',
            field=models.IntegerField(),
        ),
    ]