# Generated by Django 5.0.1 on 2024-03-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0003_alter_quiz_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="coin",
            field=models.IntegerField(default=10),
        ),
    ]
