# learning log from chapter 5 - structured data

# fantasy game inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

#list to dictionary function for fantasy fame inventory

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range (len(addedItems)):
        inventory.setdefault(addedItems[i],0) #set default is used to add default key value pairs
        inventory[addedItems[i]]=inventory[addedItems[i]]+1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)

print (inv)
print ("the nummber of ropes in the inventory is " + str(inv.get("rope",0))) #dict.get will get function looks for the key and find corresponding value

emptyDict = {}
print (emptyDict)
emptyDict["first_item"] = "i am the first item"
print (emptyDict) #adding new item into the dictionary
