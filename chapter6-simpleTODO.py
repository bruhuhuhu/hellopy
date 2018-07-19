import datetime
from collections import defaultdict

currentTime = datetime.datetime.now()
currentDate = currentTime.strftime("%d-%m-%Y")

simpleTODO = {}

def printSimpleTODO(simpleTODO):
    simpleTODO.setdefault (currentDate,["You have no items"])
    for date, items in simpleTODO.items():
        titleText = "TO DO for "+ str (date)
        print (titleText.center(50,"-"))
        for i in range (len(items)):
            print(str(i) + "." + items[i])


def addSimpleTODO(simpleTODO):
    printSimpleTODO(simpleTODO)
    print ("Add an item to the list")
    newItem = input()
    print ("Are you trying to add " + newItem + "?  (Y/N)")
    confirmation = input()
    while True:
        if confirmation == "Y":
            simpleTODO[currentDate].append(newItem)
            print (newItem + " is added to your TO DO")
            break
        elif confirmation == "N":
            print ("Item will not be added")
            break
        else:
            print ("Please enter a valid input  (Y/N)")


def startSimpleTODO(simpleTODO):
    while True:
        print ("-" * 50)
        print ("Select A Number To Use SimpleTODO, Press Enter To Exit.")
        print ("""
        1. show TO DO list
        2. add new item to TO DO list
        """)
        print ("-" * 50)
        selection = input()
        if selection == "":
            print("Program Exiting")
            break
        elif selection == "1":
            printSimpleTODO(simpleTODO)
        elif selection == "2":
            addSimpleTODO(simpleTODO)
        else:
            print("Please enter a valid input")



startSimpleTODO(simpleTODO)