# Generated by Django 5.1 on 2024-09-22 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0008_billingaddress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='oid',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='uid',
            field=models.ForeignKey(db_column='order_id', default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Order id'),
            preserve_default=False,
        ),
    ]
