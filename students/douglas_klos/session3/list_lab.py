#!/usr/bin/env python3

# Douglas Klos
# Python 210, Exercise 3
# January 24st, 2019
# list_lab.py


def series1():
    """
    Creates the specified list and displays it. Asks user for another
    fruit and adds it to end of list.  Displays list again.  Asks user
    for a number, prints it back and its coressponding fruit.
    Adds another fruit to the beginning of list using +.
    Adds another fruit to the beginning of list using insert.
    Displays all fruit in list beginning with P.
    """

    print("Series 1:")
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit)

    # Ask a user for a fruit and add to end of list.
    fruit += (input("Enter the name of fruit to be added: "),)
    print(fruit)

    # Ask user for anumber and display the number back to the use and
    # the fruit corresponding to that number.  No error trapping.
    index = input("Enter the index of fruit to print: ")
    print(f"index = {index}, fruit = {fruit[int(index)-1]}")

    # Add fruit to beginning using the "+".
    fruit = [input("Enter fruit to add at beginning of list: ")] + fruit
    print(fruit)

    # Add fruit to beginning using insert().
    fruit.insert(0, input("Enter fruit to insert at beginning of list: "))
    print(fruit)

    # Display all the fruits that begin with "P", using a for loop.
    for i in fruit:
        if i.startswith("P"):
            print(f'{i} ', end="")
    print("\n")


def series2():
    """
    Displays the list.  Removes the last fruit from the list.  Displays
    the list.  Asks the user for a fruit to delete, finds it, and
    deletes it.  Bonus section: Multiplies the list by 2, continues
    asking for a fruit until one is found, then deletes all occurances.
    """

    print("Series 2:")
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit)

    # Remove the last fruit from the list.
    fruit.pop()
    print(fruit)

    # Ask the user for a fruit, find it, and delete it.  No error trapping.
    fruit.remove(input("Enter fruit to remove from list: "))
    print(fruit)

    # Bonus: Mutiply the list by two, keep asking until a match is found.
    # Once found, delete all the occurances.
    # I wanted Applies to show up more than two times to verify it
    # would still be removed properly, hence in list twice.
    fruit = ["Apples", "Apples", "Pears", "Oranges", "Peaches"]
    fruit = fruit * 2

    print(fruit)
    kill_fruit = input("Enter fruit to remove from list: ")
    while kill_fruit in fruit:
        fruit.remove(kill_fruit)
    print(fruit)


def series3():
    """
    Asks the user "Do you like ..." for each fruit in the list.
    Fruit is printed using lowercase.  For each no, the fruit is
    deleted.  For any answer this is not yesor no, the user is
    to re-enter an answer, yes or no.
    """

    print("Series 3:")
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]

    for item in fruit[::]:
        answer = input(f"Do you like {item.lower()}?: ")
        while answer.lower() not in ('yes', 'no'):
            print("Please enter yes or no")
            answer = input(f"Do you like {item.lower()}?: ")
        if answer.lower() == "no":
            fruit.remove(item)
    print(fruit)


def series4():
    """
    Creates a new list with the contents of the original except with
    all the letters reversed.  Deletes the last item in the original
    list.  Displays the new list and original list.
    """

    print("Series 4:")
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    reversed_fruit = []
    for item in fruit:
        reversed_fruit.append(item[::-1])
    fruit.pop()
    print(reversed_fruit)
    print(fruit)
    print()


def main():
    series1()
    series2()
    series3()
    series4()


if __name__ == "__main__":
    main()
