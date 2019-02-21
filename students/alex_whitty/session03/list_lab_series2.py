#!/usr/bin/env python

fruits = ['apples', 'pears', 'oranges', 'peaches']
print(fruits)

fruits.remove('peaches')
print(fruits)

remove_fruit = input("Which fruit would you like to remove?>>>")
if remove_fruit == "apples":
    fruits.remove('apples')
    print(fruits)
elif remove_fruit == "pears":
    fruits.remove('pears')
    print(fruits)
elif remove_fruit == "oranges":
    fruits.remove('oranges')
    print(fruits)
else:
    print("Item not found!")
