# Generated by Django 4.2.16 on 2024-09-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0004_device_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
    ]
