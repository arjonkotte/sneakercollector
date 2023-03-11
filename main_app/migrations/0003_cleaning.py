# Generated by Django 4.1.7 on 2023-03-11 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cleaning",
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
                ("date", models.DateField()),
                (
                    "cleaning_level",
                    models.CharField(
                        choices=[
                            ("B", "Basic"),
                            ("I", "Intermediate"),
                            ("D", "Detailed"),
                        ],
                        default="B",
                        max_length=1,
                    ),
                ),
                (
                    "sneaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.sneaker",
                    ),
                ),
            ],
        ),
    ]
