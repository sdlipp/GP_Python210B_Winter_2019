#!/usr/bin/env python3

# series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response1 = input("Please add another fruit to the list: ")
response1 = response1.capitalize()
fruits.append(response1)
print(fruits)
fruit_count = len(fruits)
response2 = input("Pick a number between 1 and {}: ".format(fruit_count))
num = int(response2)
if num > 5:
    num = 5 #in case a number larger than 5 is entered, default to 5
y = num - 1
name_fruit = fruits[y]
print("{} is {}".format(num, name_fruit))
response3 = input("Add another fruit to the list: ")
fruits = [response3.capitalize()] + fruits
print(fruits)
response4 = input("Give me one more fruit: ")
fruits.insert(0, response4.capitalize())
print(fruits)
print("The fruits that start with the letter P are:")
for p_fruit in fruits:
    if p_fruit[0] == 'P':
        print(p_fruit)


# series 2

fruits2 = fruits
print(fruits2)
print("The last fruit will be removed")
fruits2.pop()
print(fruits2)
bye_fruit = input("Pick one more fruit from the list to remove: ")
fruits2.remove(bye_fruit.capitalize())
print(fruits2)


# series 3

fruits3 = fruits
copy_fruits3 = fruits3[:]
fruits3 = [favorites.lower() for favorites in fruits3]
copy_fruits3 = [favorites.lower() for favorites in copy_fruits3]
for favorites in fruits3:
    tasty = input("Do you like {}? ".format(favorites))
    tasty = tasty.lower() # makes the list lowercase
    
    while tasty != "no" and tasty != "yes":
        tasty = input("Please enter yes or no: ")
    if tasty == "no":
        copy_fruits3.remove(favorites)   
        
print("The fruits you like are {}:".format(copy_fruits3))
 


# series 4

fruits4 = fruits[:]
for rev_fruit in fruits4:
    print(rev_fruit[::-1])
fruits.pop()
print("This is the original list")
print(fruits)
print("This is the copy of the list")
print(fruits4)    