#!/usr/bin/env python3

'''Title: Slicing lab
Dev: Marsha Wheeler
Date: 01/29/2019
'''

'''Task 1
Write a format string that will take the following four element tuple'''
print("file_00{} : {:.2f}, {:.2e}. {:.3e}".format(2, 123.4567, 10000, 12345.67))


#Task 2
'''Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), 
and also consider f-strings if you’ve not used them already).'''
print("file_00{fileName} : {floatN1}, {intN}. {floatN2}".format(fileName = 2, floatN1 = 123.4567, intN =10000, floatN2 = 12345.67))


#Task 3
'''Dynamically Building up format strings
rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
'''
myTuple = (1,2,3,4)
l=len(myTuple)
print(('The  {} are: ' + ",".join(["{}"] * l)).format(l, *myTuple))

#Task 4
'''Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'''

fiveTuple = (4, 30, 2017, 2, 27)

print("{3:02d}, {4:02d}, {2:02d}, {0:02d}, {1:02d}".format(*fiveTuple))

#Task 5

myList = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {myList[0]} is {myList[1]} and the weight of a {myList[2]} is {myList[3]}')


#Task 6

data = (['NAME', 'AGE', 'PRICE'], ['Blue car', 1998, '$500.00'], ['Red Car', 2000, '$1000.00'], ['Motorcyle', 2019, '$25,000.00'])
#print(len(data))
#print(len(data]))

dash = '-' * 30
for i in range(len(data)):
    if i == 0:
        print(dash)
        print('{:<10s}{:>4s}{:>12s}'.format(data[i][0], data[i][1], data[i][2]))
        print(dash)
    else:
        print('{:<10s}{:>5d}{:>14s}'.format(data[i][0], data[i][1], data[i][2]))

