# Generated by Django 3.0.7 on 2020-07-01 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200629_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamprofilethree',
            name='users',
        ),
        migrations.DeleteModel(
            name='LeagueProfileThree',
        ),
        migrations.DeleteModel(
            name='TeamProfileThree',
        ),
    ]