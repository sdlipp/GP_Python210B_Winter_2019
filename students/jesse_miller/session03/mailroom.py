#!/usr/local/bin/python3
import sys

DONORS = {"Robert" : [435.56, 125.23, 357.10],
          "JD" : [123.12],
          "Chris" : [243.87, 111.32],
          "Dave" : [63.23, 422.87, 9432.01],
          "Randy" : [223.50, 8120.32],
          "Devin" : [431.12, 342.92, 5412.45],
          }

PROMPT = "\n".join(("Welcome to mailroom 0.1!",
                    "Please choose from below options:",
                    "send - If you would like to send a Thank You.",
                    "report - If you would like a report of donations totals.",
                    "quit - Exit.",
                    ">>> "))

def donor_list():
    for i in range(len(DONORS)):
        for j in range(len(DONORS[i])):
            print(DONORS[i][j], end=' ')
        print()

def mail_menu():
    PROMPT = "\n".join(("Donor and Mail Database",
                        "Please choose from below options:",
                        "list - If you would like to see a list of DONORS.",
                        "mail - If you would like to send a thank you.",
                        "new - If you would like to add a new donor.",
                        "back - If you would like to return to the main menu.",
                        ">>> "))
    while True:
        mail_input = input(PROMPT)
        if mail_input.lower() == 'list':
            donor_list()
            print("")
        if mail_input.lower() == 'mail':
            donor_list()
        if mail_input.lower() == 'new':
            donor_list()
        if mail_input.lower() == 'back':
            main()
        else:
            print("Not a valid option")

def report():
    for donor, donation1, donation2, donation3 in DONORS:
        print("{:<18}{:>8}{:>8}{:>8}".format(donor, donation1, donation2, donation3))

def goodbye():
    print("Goodbye!")
    sys.exit()

def main():
    while True:
        response = input(PROMPT)
        '''
        continuously collect user selection
        now redirect to feature functions based on the user selection
        '''
        if response.lower() == "send":
            mail_menu()
        if response.lower() == "report":
            mail_menu()
        if response.lower() == "quit":
            goodbye()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
