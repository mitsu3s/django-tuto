# Generated by Django 4.1.5 on 2023-02-20 00:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="question_text",
            new_name="question_text1",
        ),
    ]