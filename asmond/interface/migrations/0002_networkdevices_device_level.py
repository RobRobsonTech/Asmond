# Generated by Django 3.0.8 on 2020-07-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkdevices',
            name='device_level',
            field=models.IntegerField(default=1, verbose_name='Device Level'),
        ),
    ]
