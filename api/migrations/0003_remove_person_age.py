# Generated by Django 4.2.5 on 2023-09-12 23:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_person_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="age",
        ),
    ]
