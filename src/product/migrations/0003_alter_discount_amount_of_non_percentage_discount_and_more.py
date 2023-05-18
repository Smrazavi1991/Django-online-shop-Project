# Generated by Django 4.1.9 on 2023-05-18 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="amount_of_non_percentage_discount",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="discount",
            name="amount_of_percentage_discount",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(80)],
            ),
        ),
    ]