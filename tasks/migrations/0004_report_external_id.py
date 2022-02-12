# Generated by Django 4.0.1 on 2022-02-12 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_reportconsent_remove_task_reporttime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='external_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]