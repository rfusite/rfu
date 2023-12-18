# Generated by Django 4.1.7 on 2023-12-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0027_alter_footer_privacy_policy_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="CookiesConsent",
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
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=100, null=True)),
                ("title_ua", models.CharField(blank=True, max_length=100, null=True)),
                ("title_pl", models.CharField(blank=True, max_length=100, null=True)),
                ("title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("text", models.TextField(blank=True, max_length=500, null=True)),
                ("text_en", models.TextField(blank=True, max_length=500, null=True)),
                ("text_ru", models.TextField(blank=True, max_length=500, null=True)),
                ("text_ua", models.TextField(blank=True, max_length=500, null=True)),
                ("text_pl", models.TextField(blank=True, max_length=500, null=True)),
                ("text_de", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "essential_text",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "essential_text_en",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "essential_text_ru",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "essential_text_ua",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "essential_text_pl",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "essential_text_de",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text_en",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text_ru",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text_ua",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text_pl",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "analytics_text_de",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text_en",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text_ru",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text_ua",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text_pl",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "marketing_text_de",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "performance_text",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text_en",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text_ru",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text_ua",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text_pl",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "functional_text_de",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]