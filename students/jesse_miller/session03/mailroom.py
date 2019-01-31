#!/usr/local/bin/python3
import sys

donors = [["Robert", 435.56, 125.23, 357.10],
            ["JD", 123.12],
            ["Chris", 243.87, 111.32],
            ["Dave", 63.23, 422.87, 9432.01],
            ["Randy", 223.50, 8120.32],
            ["Devin", 431.12, 342.92, 5412.45],
            ]

prompt = "\n".join(("Welcome to mailroom 0.1!",
        "Please choose from below options:",
        "send - If you would like to send a Thank You.",
        "report - If you would like a report of donations totals.",
        "exit - Exit.",
        ">>> "))

def donor_list():
    for i in range(len(donors)):
        for j in range(len(donors[i])):
            print(donors[i][j], end=' ')
        print()

def mail_menu():
    prompt = "\n".join(("Donor and Mail Database",
          "Please choose from below options:",
          "list - If you would like to see a list of donors.",
          "mail - If you would like to send a thank you.",
          "new - If you would like to add a new donor.",
          "back - If you would like to return to the main menu.",
          ">>> "))
    while True:
        mail_input = input(prompt)
        if mail_input in ('list'):
            donor_list()
            print("")
        elif mail_input in ('name'):
            print(donor_list)
        elif mail_input in ('back'):
            main()
        else:
            print("Not a valid option")

#def report():

#for donor,donation1,donation2,donation3 in donors:
#    print("{:<18}{:>8}{:>8}{:>8}".format(donor,donation1,donation2,donation3))

def goodbye():
    print("Goodbye!")
    sys.exit()

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "send":
            mail_menu()
        elif response == "report":
            mail_menu()
        elif response == "exit":
            goodbye()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()




#for 1 in donors:
#    if donor,donation1,donation2,donation3 in donors:
#        print("{:<18}{:>9}{:>9}{:>9}".format(donor,donation1,donation2,donation3))
#    elif donor, donation1, donation2 in donors:
#        print("{:<18}{:>9}{:>9}".format(donor,donation1,donation2))
#    elif donor, donation1, in donors:
#        print("{:<18}{:>9}{:>9}".format(donor,donation1))
