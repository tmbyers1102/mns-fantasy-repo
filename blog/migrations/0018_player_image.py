# Generated by Django 3.0.7 on 2020-07-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_player_player_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(default='default_player.jpg', upload_to='player_pics'),
        ),
    ]