# Generated by Django 3.0.7 on 2020-06-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_team_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_logo',
            field=models.ImageField(default='default_fan_team.jpg', upload_to='fan_team_pics'),
        ),
    ]
