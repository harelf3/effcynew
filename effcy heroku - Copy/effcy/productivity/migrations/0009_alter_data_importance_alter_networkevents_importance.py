# Generated by Django 4.0.1 on 2022-02-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0008_data_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='importance',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='networkevents',
            name='importance',
            field=models.IntegerField(default=2),
        ),
    ]
