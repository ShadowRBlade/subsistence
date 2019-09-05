from os import system
from time import sleep
import string
from snippets import typethis

def openingScene():
    system("clear")
    choice = input("View Cutscene ? [Y/N]:")
    choice = choice.lower()
    if(choice == "n"):
        print("")
        # call current setting from savestate
    elif(choice == "y"):
        system("clear")
        f=open("dialogues/cutscenes/cutscene1.txt", "r")
        data = f.read()
        f.close()
        typethis(data)
    else:
        openingScene()    
