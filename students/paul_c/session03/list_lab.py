#!/usr/bin/env python3

# Series 1
print("\n*** Series 1 ***\n")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
user_fruit = input("Please type in a new fruit > ")
fruits.append(user_fruit)
print(fruits)
user_index = input("Please enter a number from 0 - 4 > ")
user_selected = fruits[int(user_index)]
print("You have selected fruit number", user_index, '"'+user_selected+'"', "from the list.")
pineapples = ["Pineapples"]
fruits = pineapples + fruits
fruits.insert(0, "Papayas")
for i in fruits:
    if i.startswith("P|p"):
        print(i)

# Series 2
print("\n*** Series 2 ***\n")
print(fruits)
fruits.pop()
print(fruits)
user_delete = input("Please choose a fruit to delete > ")
fruits.remove(user_delete)

# Series 3
print("\n*** Series 3 ***\n")
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
while True:
    user_apples = input("Do you like apples? > ")
    if user_apples != 'yes' and user_apples != 'no':
        print("Please enter yes or no.")
        continue
    elif user_apples == "no":
        fruits.remove('Apples')
        break
    else:
        break

while True:
    user_pears = input("Do you like pears? > ")
    if user_pears != 'yes' and user_pears != 'no':
        print("Please enter yes or no.")
        continue
    elif user_pears == "no":
        fruits.remove('Pears')
        break
    else:
        break

while True:
    user_oranges = input("Do you like oranges? > ")
    if user_oranges!= 'yes' and user_oranges != 'no':
        print("Please enter yes or no.")
        continue
    elif user_oranges == "no":
        fruits.remove('Oranges')
        break
    else:
        break

while True:
    user_peaches = input("Do you like peaches? > ")
    if user_peaches != 'yes' and user_peaches != 'no':
        print("Please enter yes or no.")
        continue
    elif user_peaches == "no":
        fruits.remove('Peaches')
        break
    else:
        break

print(fruits)

# Series 4
print("\n*** Series 4 ***\n")
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruits = []
for i in fruits:
    reverse = i[::-1]
    new_fruits.append(reverse)
fruits.pop()
print(fruits)
print(new_fruits)



