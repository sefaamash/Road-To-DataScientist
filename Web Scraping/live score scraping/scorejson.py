import json

with open('live-1641747907348.json') as f:
    jsondata=json.load(f)




for game in jsondata['events']:
    league = game['tournament']['name']
    hometeam = game['homeTeam']['name']
    awayteam = game['awayTeam']['name']
    homescore = game['homeScore']['current']
    awayscore = game['awayScore']['current']
    print ( league + ":" + hometeam + " " + str ( homescore ) + "  " + str ( awayscore ) + " " + awayteam )
