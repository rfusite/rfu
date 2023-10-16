# Generated by Django 4.1.7 on 2023-10-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0005_alter_card_description_alter_footer_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="name",
            field=models.CharField(default="Default Name", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="partner",
            name="logo",
            field=models.ImageField(
                default="https://via.placeholder.com/100", upload_to="partners/"
            ),
        ),
    ]
