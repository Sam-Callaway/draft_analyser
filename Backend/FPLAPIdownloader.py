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



for element in summary_data["elements"]:
    playerid = element["id"]
    
    url = "https://fantasy.premierleague.com/api/element-summary/"+str(playerid)+"/"
    playerresponse = requests.get(url)
    player_data = playerresponse.json()
    with open('backend\data\players\\'+str(playerid)+'.json', 'w') as file:
        json.dump(player_data, file)