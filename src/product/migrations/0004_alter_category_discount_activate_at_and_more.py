# Generated by Django 4.1.9 on 2023-05-18 16:34

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_discount_amount_of_non_percentage_discount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="discount_activate_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="Discount Activate at"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="discount_deactivate_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="Discount Deactivate at"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="discount_activate_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="Discount Activate at"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="discount_deactivate_at",
            field=django_jalali.db.models.jDateTimeField(
                blank=True, null=True, verbose_name="Discount Deactivate at"
            ),
        ),
    ]