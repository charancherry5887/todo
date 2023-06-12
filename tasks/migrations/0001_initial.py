# Generated by Django 4.2.2 on 2023-06-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
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
                ("userName", models.CharField(max_length=20)),
                ("task", models.CharField(max_length=200)),
                ("discription", models.CharField(max_length=1000)),
                ("createdDate", models.DateField()),
            ],
        ),
    ]
