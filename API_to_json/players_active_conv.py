import json
import requests

jsonFilePath = "players_active.json"

access_token = '538d702759d440029e450288b743e50b'

api_client = 'https://api.sportsdata.io/v3/nba/scores/json/Players?key=538d702759d440029e450288b743e50b'

r = requests.get('https://api.sportsdata.io/v3/nba/scores/json/Players?key=' + access_token)
player_json = r.json()

results = []

for player in player_json:
    PlayerID = player['PlayerID']
    FanDuelName = player['FanDuelName']

    player_str = json.dumps(player_json, indent=2)

    data = {
        'player_id': PlayerID,
        'player_full': FanDuelName,
        'player_owner': ''
    }

    results.append(data)

    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(results, indent=4))