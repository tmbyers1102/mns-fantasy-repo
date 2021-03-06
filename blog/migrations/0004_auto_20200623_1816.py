# Generated by Django 3.0.7 on 2020-06-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200623_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nbateams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('nba_team_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_salary',
        ),
        migrations.AddField(
            model_name='player',
            name='nba_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Nbateams'),
        ),
    ]
