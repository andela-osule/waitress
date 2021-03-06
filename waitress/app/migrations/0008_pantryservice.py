# Generated by Django 2.2.5 on 2020-01-11 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0007_auto_20190726_0406")]

    operations = [
        migrations.CreateModel(
            name="PantryService",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.SlackUser"
                    ),
                ),
            ],
        )
    ]
