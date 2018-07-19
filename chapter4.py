#learning log from chapter 4 onwards of automate boring things with python

animals = [ "dogs" , "cats" , "red pandas"]

print(animals[0]) #accessing from list 

zoo = [animals,[20,30,3]]

print(zoo[0][1]) #this prints the cat in the animal array

for i in range (len(animals)):
    print ("the are " + str(zoo[1][i]) + " " + zoo[0][i] + " in the zoo" )

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)