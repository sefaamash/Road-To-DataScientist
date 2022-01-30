import requests
import json
import csv
file=open("score.csv","w")
csv_writer=csv.writer(file)
csv_writer.writerow(['League','HomeTeam','Ht Score','AwayTeam','ATScore'])
url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^"
}

response = requests.request("GET", url, data=payload, headers=headers)
jsondata=json.loads(response.text)

for game in jsondata['events']:
    league = game['tournament']['name']
    hometeam = game['homeTeam']['name']
    awayteam = game['awayTeam']['name']
    homescore = game['homeScore']['current']
    awayscore = game['awayScore']['current']
    print ( league + ":" + hometeam + " " + str ( homescore ) + "  " + str ( awayscore ) + " " + awayteam )
    csv_writer.writerow([league,hometeam,awayteam,homescore,awayscore])
