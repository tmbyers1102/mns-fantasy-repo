# Generated by Django 3.0.7 on 2020-06-29 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_leagueprofilethree_teamprofilethree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_1', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_10', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_11', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_12', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_13',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_13', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_14',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_14', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_15',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_15', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_16',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_16', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_2', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_3', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_4', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_5', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_6', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_7', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_8', to='users.TeamProfileThree'),
        ),
        migrations.AlterField(
            model_name='leagueprofilethree',
            name='league_team_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='league_team_9', to='users.TeamProfileThree'),
        ),
    ]
