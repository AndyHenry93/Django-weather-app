# Generated by Django 4.1 on 2022-09-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_rename_city_forecast_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='country_code',
            field=models.CharField(default='us', max_length=10),
            preserve_default=False,
        ),
    ]
