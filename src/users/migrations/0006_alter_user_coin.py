# Generated by Django 5.0.1 on 2024-05-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_english_score_user_hobby_user_major_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="coin",
            field=models.IntegerField(default=200),
        ),
    ]
