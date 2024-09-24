# Generated by Django 5.1 on 2024-09-23 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0020_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='aid',
            field=models.ForeignKey(db_column='Aid', default=1, on_delete=django.db.models.deletion.CASCADE, to='cosmetic_app.address'),
            preserve_default=False,
        ),
    ]