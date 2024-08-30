# Generated by Django 5.1 on 2024-08-26 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0003_remove_quote_done"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("fullname", models.CharField(max_length=50)),
                ("born_date", models.CharField(max_length=50)),
                ("born_location", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name="tag",
            name="tag of username",
        ),
        migrations.RenameField(
            model_name="quote",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RemoveField(
            model_name="quote",
            name="user",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="user",
        ),
        migrations.AlterField(
            model_name="quote",
            name="quote",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quotes.author",
            ),
        ),
    ]