#!/usr/bin/env python3

'''Title: List lab
Dev: Marsha Wheeler
Date: 01/29/2019
'''

'''Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine.
Ask the user for another fruit and add it to the end of the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). 
Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
'''

print('-----Series 1 ------')

myList = ["Apples", "Pears", "Oranges", "Peaches"]
print(myList)

print('Ask the user for another fruit and add it to the end of the list.')
strFruit = input("Please enter another fruit:")
myList.append(strFruit.capitalize())
print(myList)

print('Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct')

intNum = int(input("Please choose a number between 1 and " + str(len(myList))))
print(myList[intNum - 1])

#strFruit = input("Please enter another fruit:")
#myListNew = strFruit.capitalize() + "," + str(myList).strip('[').strip(']')
#print(myListNew)

print('Add another fruit to the beginning of the list using insert() and display the list.')
strFruit = input("Please enter another fruit:")
myList.insert(0, strFruit.capitalize())
print(myList)

print('Display all the fruits that begin with “P”, using a for loop.')
for i in myList:
    if i[0] == 'P':
        print(i)


''' Series 2: 
Display the list.
Remove the last fruit from the list.
Ask the user for a fruit to delete, find it and delete it.
'''

print('-----Series 2 ------')
myList = ["Apples", "Pears", "Oranges", "Peaches"]

print('Remove the last fruit from the list.')
print(myList)
intLen = len(myList) - 1
myList.pop(intLen)
print(myList)

print('Ask the user for a fruit to delete, find it and delete it.')
strFruit = input("Please enter a fruit:")
if strFruit not in myList:
    print("That fruit is not in the list")
else:
    myList.remove(strFruit)
    print(myList)


''' Series 3: 
Ask the user for input displaying a line like “Do you like apples?” 
for each fruit in the list (making the fruit all lowercase).
'''

print('-----Series 3 ------')
myList = ["Apples", "Pears", "Oranges", "Peaches"]
print(myList)

print('Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
')
for i in myList:
    strFruit = input("Do you like " + i.lower() + "? yes/no")
    x = True
    while x is True:
        if strFruit.lower() == 'yes':
            x = True
            print(myList)
            break
        elif strFruit.lower() == 'no':
            x = True
            print(i)
            myList.remove(i)
            print(myList)
            break
        else:
            x = False
            print("Please enter yes or no")


''' Series 4: 
Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
'''

print('-----Series 4 ------')
myList = ["Apples", "Pears", "Oranges", "Peaches"]
print(myList)

newList = []
for items in myList:
    revItems = items[::-1]
    newList.append(revItems)

print(newList)
newListCopy = newList[:-1]
print(newListCopy)




