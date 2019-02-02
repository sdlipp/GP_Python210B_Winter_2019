#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

#Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print("Current Fruit List Includes: ", fruit_list)

response = input("Enter a fruit that is not on the current list: ")
fruit_list.append(response)

print("")
print("Revised Fruit List Includes: ", fruit_list)

print("")
number_response = int(input("Enter a number corresponding to a listed fruit: "))
#number_response must be a positive integer
number_response = abs(number_response)

#ensure that the entered number corresponds to a listed fruit
if number_response > len(fruit_list):
    print("There is no fruit that corresponds to that number.")
    number_response = int(input("Re-enter a number corresponding to a list element: "))
    number_response = abs(number_response) -1
    print("The number you selected corresponds to: ", fruit_list[number_response])
else:
    number_response = number_response - 1
    print("The number you selected corresponds to:",fruit_list[number_response])

print("")
fruit_list = ["Figs"] + fruit_list
print("Fruit List Update 1: ", fruit_list)

fruit_list.insert(0,"Mangos")
print("Fruit List Update 2: ", fruit_list)

print("")
print("Listed fruits beginning with P include:")
for i in fruit_list:
    if i[0] == "P":
        print(i)

#Series 2
print("")
print("Current Fruit List Includes: ", fruit_list)
fruit_list.pop()
print("Updated Fruit List Includes: ", fruit_list)
print("")

fruit_list_mult = fruit_list * 2
delete = input("Enter a fruit to delete from the list:")

#If item is not in the list, ask for the item again
while delete not in fruit_list_mult:
    delete = input("That fruit is not on the list. Re-enter a valid fruit: ")

#Find all instances of the fruit and delete it
fruit_list_mult = list(filter(lambda a: a != delete, fruit_list_mult))
print("Updated Fruit List Includes: ", fruit_list_mult)
print("")

#Series 3
fruit_list = fruit_list + [response]
#make the list items lower case
lower_fruit_list = []
for fruits in fruit_list:
    lower_fruit_list.append(fruits.lower())

for i in lower_fruit_list[:]:
    yes_no = input("Do you like " + i + "?")

    while yes_no not in ["yes", "no"]:
        yes_no = input("Please enter either yes or no:")

    if yes_no == "no":
        lower_fruit_list.remove(i)

print("")
print("Updated fruit list includes: ", lower_fruit_list)
print("")

#Series 4
fruit_list_reverse = []
for fruits in fruit_list:
    fruit_list_reverse.append(fruits[::-1])

print("List with item letters reversed: ", fruit_list_reverse)
print("")
#Delete the last item of the original list
fruit_list.pop()

fruit_list_copy = fruit_list[:]

print("Updated Fruit List: ", fruit_list)
print("Fruit List Copy: ", fruit_list_copy)
