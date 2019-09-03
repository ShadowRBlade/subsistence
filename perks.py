# for system interfacing
from os import system
# disk storage
import sqlite3

perkTitle = ['Strength    ', 'Perception  ', 'Endurance   ', 'Charisma    ', 'Intelligence', 'Agility     ', 'Luck        ']
perkCollection = []

def strength(self):
    setStrength = int(input("Enter Strength: "))
    # validate
    remain = self - setStrength
    perkCollection.append(setStrength)
    perception(remain)


def perception(self):
    setPerception = int(input("Enter Perception: "))
    # validate
    remain = self - setPerception
    perkCollection.append(setPerception)
    endurance(remain)

def endurance(self):        
    setEndurance = int(input("Enter Endurance: "))
    # validate
    remain = self - setEndurance
    perkCollection.append(setEndurance)
    charisma(remain)

def charisma(self):
    setCharisma = int(input("Enter Charisma: "))
    # validate
    remain = self - setCharisma
    perkCollection.append(setCharisma)
    intelligence(remain)

def intelligence(self):
    setIntelligence = int(input("Enter Intelligence: "))
    # validate
    remain = self - setIntelligence
    perkCollection.append(setIntelligence)
    agility(remain)

def agility(self):
    setAgility = int(input("Enter Agility: "))
    # validate
    remain = self - setAgility
    perkCollection.append(setAgility)
    luck(remain)

def luck(self):   
    setLuck = int(input("Enter Luck: "))
    # validate
    remain = self - setLuck
    perkCollection.append(setLuck)
    verify()

def setPerks(self):
    system("clear")
    print("******** Choose Your Perks ********")
    strength(self)

def verify():
    # create connection obkect
    conn = sqlite3.connect('test.db')
    # execute table creation if table does not exist
    conn.execute('''CREATE TABLE IF NOT EXISTS PERKS (PERKID INT PRIMARY KEY NOT NULL, PERK TEXT NOT NULL, VALUE INT NOT NULL);''')
    system("clear")
    status = input("Press Y to confirm: ")
    if (status == 'Y' or status == 'y'):

        print("Recording Changes...")
        for i in range(7):
        # insert into table
            statement = "INSERT INTO PERKS (PERKID, PERK , VALUE) VALUES ('" + str(i)+ "','"+str(perkTitle[i]) + "'," + str(perkCollection[i])+ ")"
            statement = str(statement)
            conn.execute(statement)
        print("DONE !")
        # display value from database
        cursor = conn.execute("SELECT perk, value from PERKS")
        for row in cursor:
            print(row [0]," ", row[1])
        
    else:
        # print("Resetting Perks..")
        setPerks(18)

    
    