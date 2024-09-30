# Generated by Django 4.2.16 on 2024-09-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0005_device_is_published"),
    ]

    operations = [
        migrations.CreateModel(
            name="SelectedCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("card_id", models.IntegerField(max_length=255)),
            ],
        ),
    ]
