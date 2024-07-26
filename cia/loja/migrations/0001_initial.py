# Generated by Django 5.0 on 2024-07-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarifas",
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
                ("origem", models.CharField(max_length=200)),
                ("destino", models.CharField(max_length=200)),
                ("escalas", models.IntegerField(default=0)),
                ("valor", models.IntegerField(default=0)),
            ],
        ),
    ]