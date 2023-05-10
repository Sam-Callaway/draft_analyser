import requests
import json

# Define the API endpoint URL
urlSummary = 'https://fantasy.premierleague.com/api/bootstrap-static/'

# Make the API request and store the response
response = requests.get(urlSummary)

# Convert the response to JSON format
summary_data = response.json()

# Save the JSON data to a file
with open('backend\data\summary.json', 'w') as file:
    json.dump(summary_data, file)

idtonamemap = {}
idtonamemap.clear()
nametoidmap = {}
nametoidmap.clear()
teammapping = {}
teammapping.clear()

for team in summary_data["teams"]:
    teamid = team["id"]
    teamname = team["name"]
    teammapping.update({teamid:teamname})


for element in summary_data["elements"]:
    playerid = element["id"]
    playerfirst = element["first_name"]
    playersecond = element["second_name"]
    webname = element["web_name"]
    teamid = element["team"]
    teamname = teammapping[teamid]
    idtonamemap.update({playerid:[playerfirst+" "+playersecond,webname,teamid,teamname]})
    nametoidmap.update({webname+"_"+teamname:playerid})
    url = "https://fantasy.premierleague.com/api/element-summary/"+str(playerid)+"/"
    playerresponse = requests.get(url)
    player_data = playerresponse.json()
    with open('backend\data\players\\'+str(playerid)+'.json', 'w') as file:
        json.dump(player_data, file)


with open('backend\data\idtonamemap.json', 'w') as file:
    json.dump(idtonamemap, file)

with open('backend\data\\nametoidmap.json', 'w') as file:
    json.dump(nametoidmap, file)

