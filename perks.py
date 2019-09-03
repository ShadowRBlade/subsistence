from os import system

perkCollection = []
perkTitle = []

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
    system("clear")
    print("******** Chosen Perks ********")
    for i in range(7):
        print(perkCollection[i])

    status = input("\nPress Y to accept: ")
    if (status == 'Y' or status == 'y'):
        print("Recording Changes...")
        # write to SQLite3 DB
    else:
        # print("Resetting Perks..")
        setPerks(18)

    
    