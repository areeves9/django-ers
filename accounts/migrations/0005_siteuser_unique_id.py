# Generated by Django 3.1.3 on 2021-01-22 22:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210117_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
