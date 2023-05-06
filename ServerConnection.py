import mysql.connector

conn = mysql.connector.connect(user='Aus', password='Alpaca44!', host='LAPTOP-PV1LLGSA', database='baseball')

def GrabTables(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='baseball' ")
    players = []
    for i in cursor:
        if('team_' not in i):
            if('player_' not in i):
                players.append(i)
    return players

def GrabAllData(connect, tname):
    cursor = connect.cursor()
    newS = tname.replace("_", " ")
    c = newS.count(" ")
    data = []
    temp = ""
    temp2 = ""
    if(c == 2):
        #Column names for the info about the player
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'player_';")
        for i in cursor:
            tempN = temp
            temp = tempN + str(i)
        name = newS[0:len(newS)-1].split(" ")
        #Column names for the stats
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{tname}';")
        for i in cursor:
            tempN = temp2
            temp2 = tempN + str(i)
        #Column names for the info about the player
        cursor.execute(f"SELECT * FROM player_ WHERE Fname = '{name[0]}' AND Lname = '{name[1]}';")
    if(c == 3):
        #Column name for the info about the team
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'team_';")
        for i in cursor:
            tempN = temp
            temp = tempN + str(i)
        name = newS[1:len(newS) - 1].split(" ")
        #Column names for the team stats
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{tname}';")
        for i in cursor:
            tempN = temp2
            temp2 = tempN + str(i)
        #Info about the team
        cursor.execute(f"Select * From team_ Where symbol = '{name[1]}'")
    data.append(temp)
    for i in cursor:
        data.append(i)
    data.append(temp2)
    #The actual stats
    cursor.execute(f"Select * From {tname}")
    for i in cursor:
        data.append(i)
    return data



