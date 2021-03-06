# Generated by Django 3.0.7 on 2020-06-22 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_team', models.CharField(max_length=100)),
                ('player_position', models.CharField(max_length=50)),
                ('player_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=100)),
                ('league_name', models.CharField(max_length=100)),
                ('league_style', models.CharField(max_length=100)),
                ('players_per_team', models.IntegerField()),
                ('league_bit_wallet_1', models.URLField()),
                ('league_bit_wallet_2', models.URLField()),
                ('league_node_1', models.URLField()),
                ('league_node_2', models.URLField()),
                ('teams_amount', models.IntegerField()),
                ('cap', models.IntegerField()),
                ('hard_cap', models.IntegerField()),
                ('lux_tax_per', models.IntegerField()),
                ('reg_season_draft_date', models.DateTimeField()),
                ('rookie_draft_date', models.DateTimeField()),
                ('eligible_draft_pick_timeframe', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_logo', models.CharField(max_length=100)),
                ('team_email_1', models.EmailField(max_length=254)),
                ('team_email_2', models.EmailField(max_length=254)),
                ('team_bit_1', models.URLField()),
                ('team_bit_2', models.URLField()),
                ('team_salary', models.IntegerField()),
                ('team_draft_picks', models.IntegerField()),
                ('team_redshirts', models.IntegerField()),
                ('team_euros', models.IntegerField()),
                ('team_reg_dues', models.IntegerField()),
                ('team_cap_fee', models.IntegerField()),
                ('team_lux_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
