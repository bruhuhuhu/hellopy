hello = "hello world"
print (hello)
print ("what is your age")
age = input()
print ("your age is " + age)

if age == "5":
    print ("you are five years old")
else: 
    print ("you are not five years old")

def enterFive(old):
    if old == "6":
        print ("are you six?")
    while True: 
        print ("enter the number 5")
        five = input()
        if five == "5":
            print("you got it right")
            break
        print ("please try again")

enterFive (age)
print("Terminating")