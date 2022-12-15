# Generated by Django 4.0.1 on 2022-01-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0004_data_importance'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=10)),
                ('website_name', models.CharField(max_length=30)),
                ('website_url', models.CharField(max_length=100)),
            ],
        ),
    ]
