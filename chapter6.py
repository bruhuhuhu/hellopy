# manipulating stings
multiLineCommenet = """
this is a test

of the multiline comment

use 3 quotation marks to do it
"""
print(multiLineCommenet)
print(multiLineCommenet[3])
multiLineCommenet = multiLineCommenet.upper() # remeber that return values have be to assigned to a variable
# there is a lower function as well. they are useful for validating user inputs
def upperCheck (toBeChecked):
    # there are other check functions such as isalpha, isalnum for other types of checks
    upperCheck = toBeChecked.isupper()
    print (upperCheck)

upperCheck(multiLineCommenet)

print (multiLineCommenet.title())


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)