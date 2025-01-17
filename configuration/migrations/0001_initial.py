# Generated by Django 4.1.1 on 2022-12-05 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
                ('speci', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.type')),
            ],
        ),
    ]
