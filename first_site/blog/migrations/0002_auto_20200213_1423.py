# Generated by Django 2.2.10 on 2020-02-13 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 13, 8, 53, 56, 845556, tzinfo=utc)),
        ),
    ]