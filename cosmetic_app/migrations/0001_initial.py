# Generated by Django 5.1 on 2024-08-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.FloatField()),
                ('pdetails', models.CharField(max_length=200, verbose_name='Product Details')),
                ('cat', models.IntegerField(choices=[(1, 'makeup products'), (2, 'hair care products'), (3, 'skin care products'), (4, 'appliances')], verbose_name='Catogory')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
    ]
