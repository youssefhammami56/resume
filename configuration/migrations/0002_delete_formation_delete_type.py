# Generated by Django 4.1.4 on 2022-12-15 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Formation',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
