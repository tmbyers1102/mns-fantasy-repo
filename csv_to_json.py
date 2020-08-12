#!/usr/bin/python

import csv, json

csvFilePath = "players.csv"
jsonFilePath = "players_done_1.json"

# read CSV and add data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        player = csvRow["player"]
        data[player] = csvRow

# write data to a JSON file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

