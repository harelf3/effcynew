# Generated by Django 4.0.1 on 2022-01-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0006_networkevents_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='desc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]