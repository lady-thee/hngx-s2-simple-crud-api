# Generated by Django 4.2.5 on 2023-09-13 01:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_remove_person_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="occupation",
        ),
        migrations.RemoveField(
            model_name="person",
            name="track",
        ),
    ]
