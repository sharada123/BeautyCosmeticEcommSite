# Generated by Django 5.1 on 2024-10-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0023_product_offvalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offvalue',
        ),
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=900, verbose_name='Product Details'),
        ),
    ]
