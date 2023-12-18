# Generated by Django 4.1.7 on 2023-12-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0015_remove_webhero_days_of_rfu_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_de",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_en",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_pl",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_ru",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_ua",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]