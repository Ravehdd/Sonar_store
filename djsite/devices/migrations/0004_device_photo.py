# Generated by Django 4.2.16 on 2024-09-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0003_rename_device_id_description_device"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="photo",
            field=models.ImageField(null=True, upload_to="photos/"),
        ),
    ]
