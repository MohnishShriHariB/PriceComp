# Generated by Django 4.2.5 on 2023-10-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricecmp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url1',
            new_name='amazon_url',
        ),
        migrations.AddField(
            model_name='product',
            name='amazon_price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='croma_price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='croma_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='flipkart_price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='flipkart_url',
            field=models.URLField(blank=True),
        ),
    ]
