# Generated by Django 4.0.1 on 2022-01-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]