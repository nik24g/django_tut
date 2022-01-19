# Generated by Django 4.0.1 on 2022-01-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('address', models.CharField(max_length=550)),
                ('problem', models.CharField(max_length=700)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
