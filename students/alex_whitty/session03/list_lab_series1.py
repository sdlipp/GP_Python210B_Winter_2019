#!/usr/bin/env python3

fruits = ['apples', 'pears', 'oranges', 'peaches']
print(fruits)

new_fruit = input("Which fruit would you like to add? >>>")
fruits.append(new_fruit)
print(fruits)

item_num = input("Which item number do you want to see? >>>")
if item_num == "1":
  print("You chose 1," + " the fruit is " + fruits[0])
elif item_num == "2":
  print("You chose 2," + " the fruit is " + fruits[1])
elif item_num == "3":
  print("You chose 3," + " the fruit is " + fruits[2])
elif item_num == "4":
  print("You chose 4," + " the fruit is " + fruits[3])
elif item_num == "5":
  print("You chose 5," + " the fruit is " + fruits[4])
else:
  print("Invalid item number.")


fruits.insert(0, 'bananas')
print(fruits)

for fruit in fruits:
    if fruit[0] == "p":
      print(fruit)
