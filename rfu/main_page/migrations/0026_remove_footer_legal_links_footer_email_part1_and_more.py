# Generated by Django 4.1.7 on 2023-12-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0025_modalwindow"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footer",
            name="legal_links",
        ),
        migrations.AddField(
            model_name="footer",
            name="email_part1",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="footer",
            name="email_part2",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="footer",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="footer",
            name="privacy_policy_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="footer",
            name="address",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]