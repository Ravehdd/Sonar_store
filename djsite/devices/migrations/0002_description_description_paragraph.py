# Generated by Django 4.2.16 on 2024-09-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="description",
            name="description_paragraph",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
