# Generated by Django 4.1.7 on 2023-12-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0014_alter_webhero_cars_count_label_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webhero",
            name="days_of_rfu",
        ),
        migrations.RemoveField(
            model_name="webhero",
            name="days_of_war",
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title_de",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title_pl",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="h1_title_ua",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="webhero",
            name="image_pattern1",
            field=models.ImageField(blank=True, null=True, upload_to="patterns/"),
        ),
        migrations.AddField(
            model_name="webhero",
            name="image_pattern2",
            field=models.ImageField(blank=True, null=True, upload_to="patterns/"),
        ),
        migrations.AddField(
            model_name="webhero",
            name="image_pattern3",
            field=models.ImageField(blank=True, null=True, upload_to="patterns/"),
        ),
    ]