# Generated by Django 5.0.1 on 2024-05-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="is_finished",
            field=models.BooleanField(default=False),
        ),
    ]
