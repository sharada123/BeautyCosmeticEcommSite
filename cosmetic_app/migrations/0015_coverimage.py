# Generated by Django 5.1 on 2024-09-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_app', '0014_remove_billingaddress_uid_delete_coverimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image', verbose_name='image name')),
            ],
        ),
    ]