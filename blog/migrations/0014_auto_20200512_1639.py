# Generated by Django 2.2.10 on 2020-05-12 11:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200420_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 11, 9, 2, 60997, tzinfo=utc)),
        ),
    ]