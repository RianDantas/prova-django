# Generated by Django 5.0 on 2024-07-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tarifas",
            name="taxaEmbarque",
            field=models.IntegerField(default=0),
        ),
    ]
