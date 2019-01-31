#!/usr/bin/env python3

# series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response1 = input("Please add another fruit to the list: ")
fruits.append(response1)
print(fruits)
fruit_count = len(fruits)
response2 = input("Pick a number between 1 and {}: ".format(fruit_count))
num = int(response2) + 1
name_fruit = 
print("{} is a {}".format(num, name_fruit))