#!/usr/local/bin/python3
"""
Beginning of my mailroom implementation.
"""
import sys

DONORS = {"Robert Smith" : [435.56, 125.23, 357.10],
          "JD Cronise" : [123.12],
          "Chris Stapleton" : [243.87, 111.32],
          "Dave Lombardo" : [63.23, 422.87, 9432.01],
          "Randy Blythe" : [223.50, 8120.32],
          "Devin Townsand" : [431.12, 342.92, 5412.45],
          }
print("")
PROMPT = "\n".join(("Welcome to mailroom 0.1!",
                    "",
                    "Please choose from below options:",
                    "send - If you would like to send a Thank You.",
                    "report - If you would like a report of donations totals.",
                    "quit - Exit.",
                    ">>> "))

SEND_PROMPT = "\n".join(("Donor and Mail Database",
                         "",
                         "Please choose from below options:",
                         "list - If you would like to see a list of DONORS.",
                         "mail - If you would like to send a thank you.",
                         "new - If you would like to add a new donor.",
                         "back - If you would like to return to the main menu.",
                         ">>> "))

def donor_list():
    '''
    This when done properly, will print the list of donor names
    '''
    print("-" * 15)
    print("List of donors: ")
    print("-" * 15)
    for donor in DONORS:
        print(donor)
    print("")
    mail_menu()

#def donor_mail():

def donor_add():
    new_donor = str(input("Enter the name of the new donor: "))
    new_don1 = int(input("Enter their first donation: "))
    new_don2 = int(input("Enter the second donation: "))
    new_don3 = int(input("Enter the third donation: "))

def mail_menu():
    '''
    This is the menu for the mail section
    '''

    while True:
        mail_input = input(SEND_PROMPT)
        if mail_input.lower() == 'list':
            print("")
            donor_list()
            print("")
        if mail_input.lower() == 'mail':
            print("")
            donor_list()
        if mail_input.lower() == 'new':
            print("")
            donor_list()
        if mail_input.lower() == 'back':
            print("")
            main()
        else:
            print("Not a valid option")
            print("")

def report():
    '''
    This will be the donation report section
    '''
    for donor, donation1, donation2, donation3 in DONORS:
        print("{:<18}{:>8}{:>8}{:>8}".format(donor, donation1, donation2, donation3))

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
    while True:
        response = input(PROMPT)
        '''
        Continuously collect user selection
        '''
        if response.lower() == "send":
            print("")
            mail_menu()
        if response.lower() == "report":
            print("")
            mail_menu()
        if response.lower() == "quit":
            print("")
            goodbye()
        else:
            print("")
            print("Not a valid option!")
            print("")

if __name__ == "__main__":
    main()
