# Generated by Django 4.2 on 2023-04-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cant_productos', models.PositiveSmallIntegerField(max_length=4)),
                ('productos', models.TextField(max_length=500)),
                ('precio', models.FloatField(max_length=6)),
            ],
        ),
    ]
