#!/usr/local/bin/python3
import sys

def main():
    print("Welcome to mailroom 0.1")
    print("")
if __name__ == "__main__":
    main()

donors = [("Robert Smith", 435.56, 125.23, 357.10),
            ("JD Cronise", 123.12, 25.05, 75.22),
            ("Chris Stapleton", 63.23, 243.87, 111.32),
            ("Dave Grohl", 63.23, 422.87, 9432.01),
            ("Randy Blythe", 223.50, 350.12, 8120.32),
            ("Devin Townsand", 431.12, 342.92, 5412.45),
            ]

def donor_list():
    for donor,donation1,donation2,donation3 in donors:
        print("{}".format(donor))
    mail_menu()

def mail_menu():
    mail_input = str(input("Please enter the donor\'s name.  Type list to see a list of donors: "))
    if (mail_input is 'list'):
        print(donor_list)
    elif(mail_input is 'name'):
        print(donor_list)
    else:
        print(donor_list)



#def report():

#for donor,donation1,donation2,donation3 in donors:
#    print("{:<18}{:>8}{:>8}{:>8}".format(donor,donation1,donation2,donation3))

def goodbye():
    print("Goodbye")
    sys.exit()

def menu():
    answer = ""
    choices = ('1', '2', '3')
    print("Please select an option from the list below:")
    print("If you would like to send a Thank You, enter 1")
    print("If you would like a report of donations totals, enter 2")
    print("To quit, enter 3")
    while answer not in choices:
        answer = str(input("Please enter 1, 2 or 3: "))
        if (answer is '1'):
            mail_menu()
        elif (answer is '2'):
            report()
        else:
            goodbye()
menu()

#for 1 in donors:
#    if donor,donation1,donation2,donation3 in donors:
#        print("{:<18}{:>9}{:>9}{:>9}".format(donor,donation1,donation2,donation3))
#    elif donor, donation1, donation2 in donors:
#        print("{:<18}{:>9}{:>9}".format(donor,donation1,donation2))
#    elif donor, donation1, in donors:
#        print("{:<18}{:>9}{:>9}".format(donor,donation1))
