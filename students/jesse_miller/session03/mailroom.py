#!/usr/local/bin/python3
"""
Beginning of my mailroom implementation.
"""
import sys


donors = {"Robert Smith" : [435.56, 125.23, 357.10],
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
                    "mail   - If you would like the mail menu.",
                    "report - If you would like a report of donations totals.",
                    "quit   - Exit.",
                    ">>> "))

SEND_PROMPT = "\n".join(("Donor and Mail Database",
                         "",
                         "Please choose from below options:",
                         "send   - If you would like to send a thank you.",
                         "list   - If you would like to see a list of donors.",
                         "back   - If you would like to return to the main menu.",
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

#def mail_menu():
#    '''
#    This is the menu for the mail section.  I have not been able to get this
#    to work properly.  When I uncomment this and comment the above out the
#    main menu loops on 'send'
#    '''
#    valid_input_mail = ("list", "send", "back")
#    while True:
#        mail_input = input(PROMPT)
#        if mail_input not in valid_input_mail:
#            print("")
#            print("Not a valid option!")
#            print("")
#        if mail_input.lower() == 'list':
#            print("")
#            donor_list()
#            print("")
#        if mail_input.lower() == 'send':
#            print("")
#            donor_mail()
#        if mail_input.lower() == 'back':
#            print("")
#            main()

def report():
    '''
    This will be the donation report section
    '''
    summary = []
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("-"*80)
    print("{:17} | {:<20} | {:<15} | {:<19}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-"*80)

    for k, v in donors.items():
        total = (sum(v))
        times = (len(v))
        avg = (sum(v) / len(v))
        summary.append([k, total, times, avg])
    summary.sort(key=lambda d: d[1], reverse=True)
    for x in summary:
        print("{:17} | ${:<18,.2f} | {:<15} |  ${:<17,.2f}".format(x[0], x[1], x[2], x[3]))
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
    for donor in donors:
        print(donor)
    print("")

def donor_mail():
    """
    This section allows the user to mail a donor
    """
    global Current_Donor
    while True:
        donor_list()
        Current_Donor = str(input("Who would you like to mail: "))
        #for donor in donors:
        if Current_Donor in donors:
            print("")
            mail_send()
        else:
            donor_add()
        mail_menu()

def donor_add():
    """
    This allows addition of new donors
    """
    if Current_Donor not in donors:
        donors[Current_Donor] = []
    d_num = int(input("How many donations were made: "))
    while d_num > 0:
        new_don = float(input("Enter their donation: "))
        donors[Current_Donor].append(new_don)
        d_num -= 1
    print("")
    mail_send()

def donor_del():
    """
    This section allows the user to delete a donor
    """
    del_donor = str(input("Enter the name of the donor to remove: "))
    del donors[del_donor]
    donor_list()

def mail_send():
    """
    This is the meat of the send process
    """
    donor_math = donors[Current_Donor]
    donor_total = sum(donor_math)
    donor_avg = len(donor_math)
    mail = ("Hello {}, \n"
            "\n"
            "We are writing to thank you for you generous donoation\n"
            "to our foundation.  Your contributions for the year \n"
            "total ${:,.2f} in {} disbursements. \n"
            "\n"
            "Again, the foundation thanks you for your support, \n"
            "and we hope to remain in contact with you in this new \n"
            "year.\n"
            "\n"
            "Sincerely, \n"
            "Ecumenical Slobs LLC \n".format(Current_Donor, donor_total, donor_avg))
    print(mail)
    mail_menu()

def main():
    '''
    The man menu and the calls to other functions
    '''
    valid_input = ("mail", "report", "quit")
    while True:
        response = input(PROMPT)
        if response not in valid_input:
            print("")
            print("Not a valid option!")
            print("")
        if response.lower() == "mail":
            print("")
            mail_menu()
        if response.lower() == "report":
            print("")
            report()
        if response.lower() == "quit":
            print("")
            goodbye()

if __name__ == "__main__":
    main()
