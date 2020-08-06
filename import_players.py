#!/usr/bin/python
import json
from blog.models import Player

csvPlayerFile = 'players_done.json'

with open(csvPlayerFile) as f:
    players_json = json.load(f)

for player in players_json:
    player = Player(player_full=player['player'],
                    player_sal_19_20=player['2019_20_salary'], player_sal_20_21=player['2020_21_salary'],
                    player_sal_21_22=player['2021_22_salary'], player_sal_22_23=player['2022_23_salary'])
    player.save()
