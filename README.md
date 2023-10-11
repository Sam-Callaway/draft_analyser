# Draft Analyser

## Description

This is a website for analysing mine and my friend's draft FPL league. FPL (Fantasy Premier League) is an online game run by the Premier League where players add footballers to their squads and earn points based on how they perform in real games.

There are a few options for analysing usual FPL leagues existing already. However, there are no services for analysing draft leagues as FPL does not make the details of these available through the API.

I am using a combination of FPL's API to get data on the Premier League and then a Python web scraper to extract information about our draft league. I'm then using Python again to process the data and Javascript for analysis functions in the back end.

I'm building a front end using React that will make API calls to my back end to retrieve data.

Since the initial data collection and processing is done using Python scripts, for the next season I will be able to simply run the scripts again to produce the analysis.
