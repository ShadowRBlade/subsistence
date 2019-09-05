from time import sleep
from sys import platform
from os import system
from os import path
import sqlite3

# Game Modules.
import perks
import districtHeungLongZi as hlz
import districtLabyrinthine as lbr
import districtSmallTown as smt
import districtTskonge as tsk

# platform check
platform = platform[:2]
if (platform == 'li'):
    # Linux Users
    system("clear")
elif(platform == 'wi'):
    # Windows Users
    system("cls")
sleep(1)


# check if database exists.
# if it does then the player is a returning player.
# else he is a new player.

if(path.exists("gamedata.db")):
    # then load saved state since db exists
    conn = sqlite3.connect('gamedata.db')
    print("Loading previous saved state.")
    rows = conn.execute('SELECT * FROM PROGRESS LIMIT 1')
    for row in rows: 
        #column 3 hold the current level of the player
        currentLevel = (row[2])
else:
    # create and write to db      
    # create connection object    
    conn = sqlite3.connect('gamedata.db')
    # execute table creation if table does not exist
    conn.execute('''CREATE TABLE IF NOT EXISTS PROGRESS (PROGRESSID INT PRIMARY KEY NOT NULL, PROGRESSLABEL TEXT NOT NULL, VALUE INT NOT NULL);''')
    
    # +++++++++++
    # Primary Key = 0
    # Level tracker; keeps track of the districts; 0 since player just begun
    # +++++++++++
    entities = [0, "Level", 0]
    
    conn.execute('''INSERT INTO PROGRESS(PROGRESSID, PROGRESSLABEL, VALUE) VALUES(?, ?, ?)''', entities)
    conn.commit()

    # set perks
    perks.setPerks()
    # reload code
    system("python3 start.py")

# branch out to the level after the value has been retreived from currentLevel
'''
if(currentLevel == 0):
    # first district
elif(currentLevel == 1):
    # second district
elif(currentLevel == 2):
    # third district
elif(currentLevel == 3):
    # fourth district
'''