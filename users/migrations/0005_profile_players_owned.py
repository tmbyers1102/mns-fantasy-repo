# Generated by Django 3.0.7 on 2020-07-13 20:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200701_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='players_owned',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
