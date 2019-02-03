#!/usr/local/bin/python3
"""
Begin Dictionary Lab
"""
import sys

cake_db = {}

def create_dict():
    cake_db["Name"] = "Chris"
    cake_db["City"] = "Seattle"
    cake_db["Cake"] = "Chocolate"
    print("")

def print_dict():
    """
    This is for printing the DB.  I will likely be calling this a lot
    """
    for k, v in cake_db.items():
        print(k,v)
    print("")

def delete_cake():
    """
    This will delete cake from the DB
    """
    del cake_db["Cake"]

def add_fruit():
    """
    This will add mango as a fruit key in the DB
    """
    cake_db["Fruit"] = "Mango"

def cake_test():
    """
    Tests for changes to the dictionary
    """
    print("Does cake exist in the dictionary?")
    if "Cake" not in cake_db:
        print("Cake is not in the dictionary")

def mango_test():
    """
    Tests for changes to the dictionary
    """
    print("Does mango exist in the dictionary?")
    if "Fruit" in cake_db:
        print("Fruit is in the dictionary")

def goodbye():
    '''
    Gracefully exits
    '''
    print("Goodbye!")
    sys.exit()

def main():
    '''
    The man menu and the calls to other functions
    '''
    print("Section 1 of Dictionary Lab")
    print("")
    print("Creating Dictionary")
    create_dict()
    print_dict()
    print("")
    print("Deleting cake")
    print("")
    delete_cake()
    print_dict()
    print("")
    print("Adding mango as a Fruit entry")
    print("")
    add_fruit()
    print_dict()
    print("")
    print("Now testing the entries in the dictionary")
    print("")
    cake_test()
    print()
    mango_test()
    print("")
    goodbye()

if __name__ == "__main__":
    main()
