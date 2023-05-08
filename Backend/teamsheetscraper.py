import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


playertags = {"John":300667,
"Joe":244043,
"Jack":490032,
"Sam":244087,
"Rory":513186,
"Tom":254648}

# Launch a browser
driver = webdriver.Chrome()

for name in playertags:
    playertag = playertags[name]
    i = 1
    while i < 36:
        # Make a request to the webpage
        
        url = "https://draft.premierleague.com/entry/"+str(playertag)+"/event/"+str(i)
        # Load the webpage
        driver.get(url)
        # Wait for the dynamic content to load
        # For example, wait for a specific element to appear
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,"PitchElement__ElementName-rzo355-2"))
        # Get the page source after the dynamic content is loaded
        html = driver.page_source
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the desired element(s) using BeautifulSoup's find() or find_all() methods
        elements = soup.find_all("div",{"class":"PitchElement__ElementName-rzo355-2"})
        # Extract the desired information from the element(s)
        for element in elements:
            print(element.text)
        i=i+1

# Close the browser when finished
driver.quit()