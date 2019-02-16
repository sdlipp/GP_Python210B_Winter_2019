import sys  # imports go at the top of the file


fruits = ['apples', 'peaches', 'oranges', 'pears']

prompt = "\n".join(("Welcome to the fruit stand!",
                    "Please choose from below options:",
                    "1 - View fruits",
                    "2 - Add a fruit",
                    "3 - The like test",
                    "4 - Remove a fruit",
                    "5 - Exit",
                    ">>> "))


def view_fruits():
    print("\n".join(fruits))


def add_fruit():
    new_fruit = input("Name of the fruit to add?")
    fruits.append(new_fruit)

def like_test():

    for fruit in fruits[:]:
        answer = input(f"Do you like {fruit}? yes/no >>>")
        if answer.lower() == 'no':
            remove_fruit()
        elif answer.lower() != 'yes':
            print('Requires (yes) or (no)')
    print(fruits)


def remove_fruit():
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
    elif remove_fruit == "peaches":
        fruits.remove('peaches')
        print(fruits)
    else:
        print("Item not found!")



def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            view_fruits()
        elif response == "2":
            add_fruit()
        elif response == "3":
            like_test()
        elif response == "4":
            remove_fruit()
        elif response == "5":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
