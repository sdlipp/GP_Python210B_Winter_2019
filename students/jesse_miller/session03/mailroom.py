#!/usr/local/bin/python3
import sys

donors = [("Robert Smith", 435.56, 125.23, 357.10),
            ("JD Cronise", 123.12, 25.05, 75.22),
            ("Chris Stapleton", 63.23, 243.87, 111.32),
            ("Dave Grohl", 63.23, 422.87, 9432.01),
            ("Randy Blythe", 223.50, 350.12, 8120.32),
            ("Devin Townsand", 431.12, 342.92, 5412.45),
            ]

prompt = "\n".join(("Welcome to mailroom 0.1!",
        "Please choose from below options:",
        "1 - If you would like to send a Thank You.",
        "2 - If you would like a report of donations totals.",
        "3 - Exit.",
        ">>> "))

def donor_list():
#        print("{}".format(donor))
#    mail_menu()
#
    print("\n".join(donors))

def mail_menu():
    prompt = "\n".join(("Donor and Mail Database",
          "Please choose from below options:",
          "list - If you would like to see a list of donors.",
          "mail - If you would like to send a thank you.",
          "new - If you would like to add a new donor.",
          "back - If you would like to return to the main menu."
          ">>> "))
    while True:
        mail_input = input(prompt)
        if mail_input in ('list'):
            print(donor_list)
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
        if response == "1":
            mail_menu()
        elif response == "2":
            mail_menu()
        elif response == "3":
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
