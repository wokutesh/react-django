# Generated by Django 5.1 on 2024-08-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_data", "0002_alter_product_category_alter_product_vendor"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_flash_sale",
            field=models.BooleanField(default=True),
        ),
    ]
