#!/usr/bin/env python3
# Lesson 03 - List Lab
# Jeremy Monroe

# Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('\n\n')
print(fruits)

new_fruit = input('Please provide another fruit: ')
fruits.append(new_fruit)

print('\n')
print(fruits)

choose_a_number = input(f"Please input a number between 1 and {len(fruits)}: ")

print('\n')
print(fruits[int(choose_a_number) - 1])

new_fruit = input('Please provide another fruit: ')

fruits.insert(0, new_fruit)

print(fruits)

for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit, end=', ')




# Series 2
print("\n\nSERIES 2 BEGINS")
series_2_fruits = fruits[:]
print(series_2_fruits)

series_2_fruits.pop()

print(series_2_fruits)

# series 2 bonus
in_list = 0
while not in_list:
    delete_me = input('Tell me which fruit to delete: ')
    if delete_me in series_2_fruits:
        in_list = 1
    else:
        print("THAT FRUIT DOESN'T EXIST")

# series_2_fruits.remove(delete_me)

series_2_fruits = series_2_fruits[:] + series_2_fruits[:]
print(series_2_fruits)

while delete_me in series_2_fruits:
    series_2_fruits.remove(delete_me)

print(series_2_fruits)




# Series 3
print("\n\nSERIES 3 BEGINS")

series_3_fruits = fruits[:]
series_3_fruits_copy = series_3_fruits[:]

for fruit in series_3_fruits:
    yes_or_no = input(f"\nDo you like {fruit}?\nYes or No:")
    if yes_or_no.lower() == 'no':
        series_3_fruits_copy.remove(fruit)

    while yes_or_no.lower() != 'yes' and yes_or_no.lower() != 'no':
        yes_or_no = input('ENTER YES OR NO: ')

series_3_fruits = series_3_fruits_copy[:]
print()
print(series_3_fruits)




# Series 4
print('\n\nSERIES 4 BEGINS')
series_4_fruits = fruits[:]
reverse_fruits = []

for fruit in series_4_fruits:
    reverse_fruits.append(fruit[::-1])

series_4_fruits.pop()
print(series_4_fruits)
print(reverse_fruits)