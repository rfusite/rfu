# Generated by Django 4.1.7 on 2023-10-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0004_paymentmethod_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="footer",
            name="address",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="mission",
            name="text",
            field=models.TextField(),
        ),
    ]
