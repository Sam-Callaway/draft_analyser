from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

with open('backend\data\\nametoidmap.json') as namemap:
  namemap2 = namemap.read()

nametoidmap = json.loads(namemap2)

managertags = {"John":300667,
"Joe":244043,
"Jack":490032,
"Sam":244087,
"Rory":513186,
"Tom":254648}

teamsheets = {}
teamsheets.clear()
for name in managertags:
    teamsheets[name] = {1:{"field":[],"bench":[]}}
    i = 2
    while i < 39:
        teamsheets[name].update({i:{"field":[],"bench":[]}})
        i = i+1

# Launch a browser
driver = webdriver.Chrome()

for name in managertags:
    managertag = managertags[name]
    i = 1
    while i < 2:
        url = "https://draft.premierleague.com/entry/"+str(managertag)+"/event/"+str(i)
        # Load the webpage
        driver.get(url)
        # Wait for the dynamic content to load
        # For example, wait for a specific element to appear
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"PitchElement__ElementName-rzo355-2"))
        # Get the page source after the dynamic content is loaded
        html = driver.page_source
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the desired element(s) using BeautifulSoup's find() or find_all() methods
        elements = soup.find_all("div",{"class":"PitchElement__ElementName-rzo355-2"})
        # Extract the desired information from the element(s)
        for element in elements:
            playername = element.text
            parentElement = element.parent
            imgElement = parentElement.previous_sibling
            teamname = imgElement.get('title')
            playerid = nametoidmap[playername+"_"+teamname]
            print(playername)
            print(teamname)  
            print(playerid)               

        i=i+1

# Close the browser when finished
driver.quit()

with open('backend\data\\teamsheets.json', 'w') as file:
    json.dump(teamsheets, file)

