import json
import csv

# Double gameweek rounds have two entries inplayer history array
def playerScores():
    with open('backend\data\playerScore.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PlayerID','GW1','GW2','GW3','GW4','GW5','GW6','GW7','GW8','GW9','GW10','GW11','GW12','GW13','GW14','GW15','GW16','GW17','GW18','GW19','GW20','GW21','GW22','GW23','GW24','GW25','GW26','GW27','GW28','GW29','GW30','GW31','GW32','GW33','GW34','GW35','GW36','GW37','GW38'])
        i = 1
        while i < 779:
            with open('backend\data\players\\'+str(i)+'.json') as p:
                playerData = json.load(p)
                scoreList = [i]
                j = 0
                while j < 38:
                    scoreList.append(0)
                    j = j+1
                for round in playerData["history"]:
                    roundNum = round["round"]
                    scoreList[roundNum] = scoreList[roundNum] + round["total_points"]
            writer.writerow(scoreList)
            i = i+1


def scorer(): 
    with open('backend\data\\teamsheets.json') as ts:
        ts2 = ts.read()

    teamsheets = json.loads(ts2)
    with open('backend\data\playerScore.csv', 'r', newline='') as pl:
        playerScores = list(csv.reader(pl))
        with open('backend\data\weeklyscore.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Manager','GW1','GW2','GW3','GW4','GW5','GW6','GW7','GW8','GW9','GW10','GW11','GW12','GW13','GW14','GW15','GW16','GW17','GW18','GW19','GW20','GW21','GW22','GW23','GW24','GW25','GW26','GW27','GW28','GW29','GW30','GW31','GW32','GW33','GW34','GW35','GW36','GW37','GW38'])
            for manager in teamsheets:
                i = 1
                managerrow = [manager]
                while i < 39:
                    currentGW = str(i)
                    weeklyscore = 0
                    for id in teamsheets[manager][currentGW]["pitch"]:                        
                        playerscore = int(playerScores[id][i])
                        weeklyscore = weeklyscore + playerscore
                    managerrow.append(weeklyscore)
                    i = i+1               
                writer.writerow(managerrow)
        with open('backend\data\\totalscore.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Manager','GW1','GW2','GW3','GW4','GW5','GW6','GW7','GW8','GW9','GW10','GW11','GW12','GW13','GW14','GW15','GW16','GW17','GW18','GW19','GW20','GW21','GW22','GW23','GW24','GW25','GW26','GW27','GW28','GW29','GW30','GW31','GW32','GW33','GW34','GW35','GW36','GW37','GW38'])
            for manager in teamsheets:
                i = 1
                managerrow = [manager]
                weeklyscore = 0
                while i < 39:
                    currentGW = str(i)
                    for id in teamsheets[manager][currentGW]["pitch"]:
                        playerscore = int(playerScores[id][i])
                        weeklyscore = weeklyscore + playerscore
                    managerrow.append(weeklyscore)
                    i = i+1                    
                writer.writerow(managerrow)

playerScores() 
scorer()
