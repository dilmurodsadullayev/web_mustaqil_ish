# Generated by Django 5.0.4 on 2024-04-27 10:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kinds",
            old_name="kind",
            new_name="kinds",
        ),
    ]
