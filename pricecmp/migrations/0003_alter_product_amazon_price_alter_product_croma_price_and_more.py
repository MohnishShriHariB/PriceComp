# Generated by Django 4.2.5 on 2023-10-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricecmp', '0002_rename_url1_product_amazon_url_product_amazon_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amazon_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='croma_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='flipkart_price',
            field=models.IntegerField(null=True),
        ),
    ]