# Generated by Django 5.1 on 2024-09-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0013_billingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='uid',
        ),
        migrations.DeleteModel(
            name='CoverImage',
        ),
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=200, verbose_name='Product Details'),
        ),
        migrations.DeleteModel(
            name='BillingAddress',
        ),
    ]
