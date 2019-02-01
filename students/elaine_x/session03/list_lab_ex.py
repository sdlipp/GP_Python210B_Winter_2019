#!/usr/bin/env python3

'''
##########################
#Python 210
#Session 03 - List Lab
#Elaine Xu
#Jan 28,2019
###########################
'''

############# Series 1 ################################
print("Series 1\nList of Fruit:")
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(FRUITS)

#Ask the user for another fruit and add it to the end of the list
FRUIT = input('Enter another fruit: ')
FRUITS.append(FRUIT)
print(FRUITS)

#Ask user for a number, display the number and the fruit corresponding to the number
NUMBER = int(input('Enter an index number (1 is first): '))
print("The "+ str(NUMBER) +"th fruit is "+FRUITS[NUMBER-1])

#Add another fruit to the beginning of the list using “+” and display the list
print()
print('Adding "Kiwi" to the beginning of the list')
FRUITS = ['Kiwi'] + FRUITS
print(FRUITS)

#Add another fruit to the beginning of the list using insert() and display the list
print()
print('Adding "Banana" to the beginning of the list')
FRUITS.insert(0, 'Banana')
print(FRUITS)

#Display all the fruits that begin with “P”, using a for loop
print()
print('Display all the fruits that begin with "P"')
for item in FRUITS:
    if item[0] == "P":
        print(item)


############# Series 2 ################################
print()
print("Series 2\nList of Fruit:")
FRUITS2 = FRUITS[:]
print(FRUITS2)

#Remove the last fruit from the list
print()
FRUITS2.pop()
print("Deleting the last fruit:")
print(FRUITS2)

#Ask the user for a fruit to delete, find it and delete it
print()
FRUIT_DELETE = input("Enter a fruit to delete: ")
FRUITS2.remove(FRUIT_DELETE)
print(FRUITS2)

#Bonus: List*2. Keep asking until a match is found. Once found, delete all occurrences
print()
FRUITS2B = FRUITS[:]*2
print('List * 2:', FRUITS2B)
FRUIT_DELETE2 = input("Bonus: Enter a fruit to delete: ")
while FRUIT_DELETE2 in FRUITS2B:
    FRUITS2B.remove(FRUIT_DELETE2)
print(FRUITS2B)


############# Series 3 ################################
print()
print("Series 3\nList of Fruit:")
FRUITS3 = FRUITS[:]
print(FRUITS3)
FRUITS3_COPY = FRUITS3[:]

for fruit in FRUITS3:
    choice = ''
    while choice.lower() != 'yes' and choice.lower() != 'no':
        choice = input("Do you like " + fruit.lower() + "? (yes or no):")
        if choice.lower() == 'no':
            FRUITS3_COPY.remove(fruit)
print(FRUITS3_COPY)


############# Series 4 ################################
print()
print("Series 4\nList of Fruit:")
FRUITS4 = FRUITS[:]
print(FRUITS4)

#Make a new list with the contents of the original, but with all the letters in each item reversed
def reverse(in_str):
    '''reverse an input string'''
    string = ''
    for letter in in_str:
        string = letter + string
    return string
FRUITS5 = ['']*len(FRUITS4)
for i, fruit in enumerate(FRUITS4):
    FRUITS5[i] = reverse(FRUITS4[i])
print("Reversed:", FRUITS5)

#Delete the last item of the original list. Display the original list and the copy
print()
print("Original:", FRUITS4)
FRUITS4.pop()
print("Copy with last item deleted:", FRUITS4)
