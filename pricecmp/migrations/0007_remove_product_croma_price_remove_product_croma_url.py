# Generated by Django 4.2.5 on 2023-10-09 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricecmp', '0006_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='croma_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='croma_url',
        ),
    ]