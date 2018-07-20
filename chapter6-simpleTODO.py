import datetime
from collections import defaultdict

currentTime = datetime.datetime.now()
currentDate = currentTime.strftime("%d-%m-%Y")

simpleTODO = {}

def printSimpleTODO(simpleTODO):
    simpleTODO.setdefault (currentDate,[])
    for date, items in simpleTODO.items():
        titleText = "TO DO for "+ str (date)
        print (titleText.center(50,"-"))
        currentDateItemList = simpleTODO.get(currentDate)
        if len(currentDateItemList) == 0:
            print ("""
            You have no task in your TO DO list
            """)
        else: 
            for i in range (len(items)):
                index = i+1
                print(str(index) + "." + items[i])
            print ("""
            You have reacehed the end of your TO DO list
            """)

def addSimpleTODO(simpleTODO):
    printSimpleTODO(simpleTODO)
    print ("Add an item to the list")
    newItem = input()
    print ("Are you trying to add " + newItem + "?  (Y/N)")
    while True:
        confirmation = input()
        if confirmation == "Y":
            simpleTODO[currentDate].append(newItem)
            print (newItem + " is added to your TO DO")
            break
        elif confirmation == "N":
            print ("Item will not be added")
            break
        else:
            print ("Please enter a valid input  (Y/N)")

def removeSimpleTODO(simpleTODO):
    currentDateItemList = simpleTODO.get(currentDate)
    if len(currentDateItemList) == 0:
        print ("""
        You have no task in your To DO list for removal
        """)
    else:
        printSimpleTODO(simpleTODO)
        print ("Remove an item to the list")
        removeItemIndex = input()
        removeItem = currentDateItemList[int(removeItemIndex) - 1]
        print ("Are you trying to remove " + removeItem + "? (Y/N)")
        while True:
            confirmation = input()
            if confirmation == "Y":
                del currentDateItemList[int (removeItemIndex) - 1]
                print (removeItem + " is removed from your TO DO list")
                break
            elif confirmation == "N":
                print ("Item will not be removed")
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
        3. remove item from TO DO list
        """)
        print ("-" * 50)
        selectionIndex = input()
        if selectionIndex == "":
            print("Program Exiting")
            break
        elif selectionIndex == "1":
            printSimpleTODO(simpleTODO)
        elif selectionIndex == "2":
            addSimpleTODO(simpleTODO)
        elif selectionIndex == "3":
            removeSimpleTODO(simpleTODO)
        else:
            print("Please enter a valid input")

startSimpleTODO(simpleTODO)