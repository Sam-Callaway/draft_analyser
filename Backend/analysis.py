import json
import csv


def scorer(): 
    with open('backend\data\\teamsheets.json') as ts:
        ts2 = ts.read()

    teamsheets = json.loads(ts2)

    with open('backend\data\weeklyscore.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Manager','GW1','GW2','GW3','GW4','GW5','GW6','GW7','GW8','GW9','GW10','GW11','GW12','GW13','GW14','GW15','GW16','GW17','GW18','GW19','GW20','GW21','GW22','GW23','GW24','GW25','GW26','GW27','GW28','GW29','GW30','GW31','GW32','GW33','GW34','GW35','GW36','GW37','GW38'])
        for manager in teamsheets:
            i = 1
            currentGW = str(i)
            managerrow = [manager]
            weeklyscore = 0
            while i < 39:
                for id in teamsheets[manager][currentGW]["pitch"]:
                    with open('backend\data\players\\'+str(id)+'.json') as p:
                        playerdata = json.load(p)
                        playerscore = playerdata["history"][i]["total_points"]
                        weeklyscore = weeklyscore + playerscore
                managerrow.append(weeklyscore)
                i = i+1                    
            writer.writerow(managerrow)
scorer()