# Generated by Django 4.0.1 on 2022-02-12 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_report_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), help_text='Times are in UTC', null=True),
        ),
    ]
