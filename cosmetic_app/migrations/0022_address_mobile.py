# Generated by Django 5.1 on 2024-09-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0021_order_aid'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile',
            field=models.CharField(default=8888888888, max_length=100, verbose_name='Mobile Number'),
            preserve_default=False,
        ),
    ]
