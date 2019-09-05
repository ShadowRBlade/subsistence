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

def setPerks():
    system("clear")
    # clear or reset array to prevent garbage values from residing in the array
    perkCollection.clear()
    initial = 18 # set to a value of 18
    print("******** Choose Your Perks ********")
    print("     18 Perk Points Available     ")
    strength(initial)

def verify():
    # check if sum is 18 else call setPerks
    if(sum(perkCollection) != 18):
        print("Invalid Combination. Perks should amount to 18")
        input("Press any key to continue")
        setPerks()

    # create connection object
    conn = sqlite3.connect('gamedata.db')
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
            try:
                conn.execute(statement)               
                # commit added
                conn.commit()
            except:
                print("Cannot reset perks once set.\n")
                break  

        # display value from database
        print("\nChosen Perks:")
        cursor = conn.execute("SELECT PERK, VALUE from PERKS")
        for row in cursor:
            print(row[0]," | ", row[1])
        
    else:
        # print("Resetting Perks..")
        setPerks()
