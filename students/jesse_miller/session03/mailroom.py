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
                    "mail - If you would like the mail menu.",
                    "report - If you would like a report of donations totals.",
                    "quit - Exit.",
                    ">>> "))

SEND_PROMPT = "\n".join(("Donor and Mail Database",
                         "",
                         "Please choose from below options:",
                         "send - If you would like to send a thank you.",
                         "list - If you would like to see a list of donors.",
                         "back - If you would like to return to the main menu.",
                         ">>> "))

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
        if mail_input.lower() == 'send':
            print("")
            donor_mail()
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
    summary= []
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("-"*80)
    print("{:17} | {:<20} | {:<15} | {:<19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-"*80)

    for k,v in DONORS.items():
        donor = k
        total = (sum(v))
        times = (len(v))
        avg = (sum(v) / len(v))
        summary.append([k, total, times, avg])
    summary.sort(key=lambda d: d[1], reverse=True)
    for x in summary:
        print("{:17} |  ${:<18,.2f} | {:<15} |  ${:<17,.2f}".format(x[0], x[1], x[2], x[3]))
    print("-"*80)
    print("")
    main()

def goodbye():
    '''
    Gracefully exits
    '''
    print("Goodbye!")
    sys.exit()

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
    #mail_menu()

def donor_mail():
    """
    This section allows the user to mail a donor
    """
    while True:
        donor_list()
        donor_send = str(input("Who would you like to mail: "))
        for donor in DONORS:
            if donor_send == donor:
                mail_send()
            else:
                new_donor = donor_send
                d_num = int(input("How many donations were made: "))
                if d_num == 1:
                    new_don1 = float(input("Enter their first donation: "))
                    DONORS[new_donor] = new_don1
                if d_num == 2:
                    new_don1 = float(input("Enter their first donation: "))
                    new_don2 = float(input("Enter the second donation: "))
                    DONORS[new_donor] = new_don1, new_don2
                if d_num == 3:
                    new_don1 = float(input("Enter their first donation: "))
                    new_don2 = float(input("Enter the second donation: "))
                    new_don3 = float(input("Enter the third donation: "))
                    DONORS[new_donor] = new_don1, new_don2, new_don3
                else:
                    print("Please enter only 1, 2 or 3")
                donor_list()
            mail_menu()

def mail_send():
    """
    This is the meat of the send process
    """
    mail_menu()

def donor_del():
    """
    This section allows the user to delete a donor
    """
    del_donor = str(input("Enter the name of the donor to remove: "))
    del DONORS[del_donor]
    donor_list()

def main():
    '''
    The man menu and the calls to other functions
    '''
    while True:
        response = input(PROMPT)
        if response.lower() == "mail":
            print("")
            mail_menu()
        if response.lower() == "report":
            print("")
            report()
        if response.lower() == "quit":
            print("")
            goodbye()
        else:
            print("")
            print("Not a valid option!")
            print("")

if __name__ == "__main__":
    main()
