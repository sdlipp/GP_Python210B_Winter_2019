#!/usr/bin/env python3

#LIST LAB

#SERIES 1
Fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruits:',Fruits)

#Ask the user for another fruit.
New_Fruit = input('Add another fruit: ')
Fruits.append(New_Fruit)
print(Fruits)

#Ask user for a number.
Number = int(input('Pick a number between 1-5:'))
print('Number '+str(Number)+' corresponds to '+Fruits[Number-1])

#Add another fruit to the beginning of the list using “+”
print('Adding another fruit to the beginning of the list')
Fruits = ['Mango']+Fruits
print(Fruits)

#Add another fruit to the beginning of the list using insert()
print('Adding another fruit to the beginning of the list')
Fruits.insert(0, 'Pineapple')
print(Fruits)

#Display all the fruits that begin with “P”, using a for loop.
print('All the fruits that begin with "P":')
for item in Fruits:
    if item[0] == 'P':
        print(item)


#SERIES 2
Fruits_2 = Fruits[:]
print('Fruits:',Fruits_2)

#Remove the last fruit from the list
Fruits_2.pop()
print('Removing the last fruit:')
print(Fruits_2)

#Ask the user for a fruit to delete
Delete = input('Pick a fruit to delete:')
Fruits_2.remove(Delete)
print(Fruits_2)

#Bonus
Fruits_2_bonus = Fruits[:]*2
print('Fruits_Doubled:', Fruits_2_bonus)
Delete_2 = input('Pick another fruit to delete:')
while Delete_2 in Fruits_2_bonus:
    Fruits_2_bonus.remove(Delete_2)
print(Fruits_2_bonus)


#SERIES 3
Fruits_3 = Fruits[:]
print('Fruits:',Fruits_3)

#Ask the user “Do you like ...?”
for item in Fruits_3:
    answer = ''
    while answer.lower()!='no' and answer.lower()!='yes':
        answer = input('Do you like '+item.lower()+'? yes/no:')
        if answer.lower()=='no':
            Fruits_3.remove(item)
print(Fruits_3)


#SERIES 4
Fruits_4 = Fruits[:]
print('Fruits:',Fruits_4)

#Make a new list with original reversed
'''
def func(seq):
    answer= ''
    for item in seq:
        answer.append(item[::-1])
    return item
print('Reversed:')
print(func(Fruits_4))
#I can't figure this out
'''

#Delete the last item of the original list
print('Original list:')
print(Fruits_4)

Fruits_4.pop()
print('Original after last item deleted:')
print(Fruits_4)
