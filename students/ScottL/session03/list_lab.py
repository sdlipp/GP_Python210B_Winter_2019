#!/usr/bin/env python3

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


def display_list(sequence):
    """Display a header and list of individual items in the list of fruit."""
    print("\nFruit List\n" + "-" * 10)
    for item in sequence:
        print(item)


def display_p_fruits():
    """Display only items in the fruit list that start with the letter 'P'."""
    for item in fruit_list:
        if item[0].lower() == "p":
            print(item)

def remove_item():
    """Receive input from the user on which item to remove from a list"""
    flag = False
    while flag is False:
        item_delete = input("\nWhich item would you like to delete? Type the name of the item: ")
        for item in fruit_list:
            if item == item_delete:
                fruit_list.remove(item_delete)
                flag = True


def check_likability():
    """Receive user input on all item in fruit list to decide whether or not to keep them"""
    for item in fruit_list:
        while True:
            user_response = input("Do you like {}? Enter yes or no: ".format(item.lower())).lower()
            if not (user_response == "no" or user_response == "yes"):
                continue
            elif user_response == "no":
                fruit_list.remove(item)
            break


def reverse_order():
    """Return a copy of the fruit list with all the names for the items reversed (e.g. Apple --> elppA"""
    reverse_names = []
    for item in fruit_list:
        reverse_names.append(item[::-1])
    return reverse_names



display_list(fruit_list)
fruit_list.append(input("\nEnter a fruit to add to the list: "))
display_list(fruit_list)
user_select_number = int(input("\nEnter a number between 1 and {} to display a fruit: ".format(len(fruit_list))))
print(fruit_list[user_select_number - 1])
fruit_list = [input("\nEnter a fruit to add to the list: ")] + fruit_list
fruit_list.insert(0, input("\nEnter a fruit to add to the list: "))
display_p_fruits()
display_list(fruit_list)
fruit_list.pop()
display_list(fruit_list)
remove_item()
check_likability()
display_list(fruit_list)
reverse_fruit_list = reverse_order()
fruit_list.pop()
display_list(fruit_list)
display_list(reverse_fruit_list)
