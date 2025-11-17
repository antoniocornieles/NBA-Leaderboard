from pprint import PrettyPrinter
import requests

url = "https://api-nba-v1.p.rapidapi.com/standings"

printer = PrettyPrinter()

querystring = {"league":"standard","season":"2025"}

headers = {
	"X-RapidAPI-Key": "9a7e630c53msh1a6700f37ce9085p1fc4abjsn42744c4ee10f",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

teams = response.json()['response']
teams.sort(key=lambda x: float(x['win']['percentage']), reverse = True)
#still need to address tiebreakers

print("NBA League Standings\n")

for i, team in enumerate(teams):
    name = team['team']['name']
    wins = team['win']['total']
    loss = team['loss']['total']
    pct = team['win']['percentage']
    gb = team['gamesBehind']
    homeW = team['win']['home']
    homeL = team['loss']['home']
    home = str(homeW) + "-" + str(homeL)
    awayW = team['win']['away']
    awayL = team['loss']['away']
    away = str(awayW) + "-" + str(awayL)
    L10W = team['win']['lastTen']
    L10L = team['loss']['lastTen']
    L10 =  str(L10W) + "-" + str(L10L)
    Strk = "W" + str(team['streak']) if str(team['winStreak']) == "True" else "L" + str(team['streak'])

    #missing some stats compared to official NBA and could be formatted better
    print(str(i + 1) + ".", name, str(wins) + "W", str(loss) + "L",  "W% " + str(pct),
    "Home " + home, "Away " + away, "L10 " + L10, "Streak " + Strk)

'''printer.pprint(response.json())'''

