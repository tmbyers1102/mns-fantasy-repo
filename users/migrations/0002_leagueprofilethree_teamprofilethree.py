# Generated by Django 3.0.7 on 2020-06-29 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamProfileThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasy_team_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueProfileThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasy_league_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('group', models.ManyToManyField(blank=True, to='auth.Group')),
                ('league_team_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_1', to='users.TeamProfileThree')),
                ('league_team_10', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_10', to='users.TeamProfileThree')),
                ('league_team_11', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_11', to='users.TeamProfileThree')),
                ('league_team_12', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_12', to='users.TeamProfileThree')),
                ('league_team_13', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_13', to='users.TeamProfileThree')),
                ('league_team_14', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_14', to='users.TeamProfileThree')),
                ('league_team_15', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_15', to='users.TeamProfileThree')),
                ('league_team_16', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_16', to='users.TeamProfileThree')),
                ('league_team_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_2', to='users.TeamProfileThree')),
                ('league_team_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_3', to='users.TeamProfileThree')),
                ('league_team_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_4', to='users.TeamProfileThree')),
                ('league_team_5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_5', to='users.TeamProfileThree')),
                ('league_team_6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_6', to='users.TeamProfileThree')),
                ('league_team_7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_7', to='users.TeamProfileThree')),
                ('league_team_8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_8', to='users.TeamProfileThree')),
                ('league_team_9', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_9', to='users.TeamProfileThree')),
            ],
        ),
    ]
