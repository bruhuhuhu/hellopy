# learning log from Automate boring things with python
# chatper 2 - control flow
import random

hello = "hello world"
print (hello)
print ("what is your age")
age = input()
print ("your age is " + age)

if age == "5":
    print ("you are five years old")
else: 
    print ("you are not five years old")

for i in range (1,10):
    print (" " * (10 - i) + "_" * (i * 2))

def printFive (enter_number):
    if enter_number == "5":
        return print("you entered a 5")
    else:
        return print("you did not key in a 5", "you need to key in a 5" , sep = " ,")

def enterFive(entered_number):
    if entered_number == "6":
        print ("you keyed 6 for your age")
    while True: 
        print ("enter the number 5")
        five = input()
        printFive(five)
        if five == "5":
            print("you got it right")
            break
        print ("please try again")

enterFive (age)

print ("i am giving you a random number between 1 to 100", end = " and " )
print ("the random number is " + str(random.randint(1,100)))

print("\n\nTerminating\n")