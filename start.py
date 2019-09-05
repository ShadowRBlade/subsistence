from time import sleep
from sys import platform
from os import system
from os import path
import perks
import sqlite3

platform = platform[:2]
if (platform == 'li'):
    print("Running on Linux")
elif(platform == 'wi'):
    print("Running on Windows")
sleep(2)


if(path.exists("gamedata.db")):
    # then load saved state since db exists
    print("Loading previous saved state.")
else:
    # create and write to db      
    # create connection object    
    conn = sqlite3.connect('gamedata.db')
    # execute table creation if table does not exist
    conn.execute('''CREATE TABLE IF NOT EXISTS PROGRESS (PROGRESSID INT PRIMARY KEY NOT NULL, PROGRESSLABEL TEXT NOT NULL, VALUE INT NOT NULL);''')
    # set perks
    perks.setPerks()
    
