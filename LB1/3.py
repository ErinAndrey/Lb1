players=['Player1','Player2','Player3','Player4','Player5','Player6']
Summa=len(players)
Playersinteam =Summa//2
team1=players[0:Playersinteam]
team2=players[Playersinteam:]
print(team1,team2)