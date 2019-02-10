#!/usr/local/bin/python3
"""
Beginning of my mailroom implementation.
"""
import sys
import os
import datetime

donors = {"Robert Smith": [435.56, 125.23, 357.10],
          "JD Cronise": [123.12],
          "Chris Stapleton": [243.87, 111.32],
          "Dave Lombardo": [63.23, 422.87, 9432.01],
          "Randy Blythe": [223.50, 8120.32],
          "Devin Townsand": [431.12, 342.92, 5412.45],
          }

PROMPT = "\n".join(("Welcome to mailroom 0.5!",
                    "",
                    "Please choose from below options:",
                    "report - If you would like a report of donations totals.",
                    "send - If you would like to send a thank you.",
                    "all  - Create files for mails to all donors",
                    "list - If you would like to see a list of donors.",
                    "quit   - Exit.",
                    ">>> "))

VALID_INPUT = ("report", "quit", "list", "send", "all")


def report():
    '''
    This will be the donation report section
    '''
    summary = []
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("-"*80)
    print("{:17} | {:<20} | {:<15} | {:<19}".format(headers[0], headers[1], \
    headers[2], headers[3]))
    print("-"*80)

    for k, v in donors.items():
        total = (sum(v))
        times = (len(v))
        avg = (sum(v) / len(v))
        summary.append([k, total, times, avg])
    summary.sort(key=lambda d: d[1], reverse=True)
    for x in summary:
        print("{:17} | ${:<18,.2f} | {:<15} |  ${:<17,.2f}".format(x[0], x[1], \
        x[2], x[3]))
    print("-"*80)
    print("")


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
    print("\n")
    print("-" * 15)
    print("List of donors: ")
    print("-" * 15)
    for donor in donors:
        print(donor)
    print("-" * 15)
    print("\n")


def donor_mail():
    """
    This section allows the user to mail a donor
    """
    current_donor = ""
    donor_list()
    current_donor = str(input("Who would you like to mail: "))
    if current_donor in donors:
        print("")
        mail_send(current_donor)
    else:
        donor_add(current_donor)


def donor_add(current_donor):
    """
    This allows addition of new donors
    """
    if current_donor not in donors:
        donors[current_donor] = []
    d_num = int(input("How many donations were made: "))
    while d_num > 0:
        new_don = float(input("Enter their donation: "))
        donors[current_donor].append(new_don)
        d_num -= 1
    mail_send(current_donor)


def donor_del():
    """
    This section allows the user to delete a donor
    """
    del_donor = str(input("Enter the name of the donor to remove: "))
    del donors[del_donor]
    donor_list()


def mail_send(current_donor):
    """
    This is the meat of the send process
    """
    donor_math = donors[current_donor]
    donor_total = sum(donor_math)
    donor_avg = len(donor_math)
    mail = ("Hello {}, \n"
            "\n"
            "We are writing to thank you for you generous donation\n"
            "to our foundation.  Your contributions for the year \n"
            "total ${:,.2f} in {} disbursements. \n"
            "\n"
            "Again, the foundation thanks you for your support, \n"
            "and we hope to remain in contact with you in this new \n"
            "year.\n"
            "\n"
            "Sincerely, \n"
            "Ecumenical Slobs LLC \n".format(current_donor, donor_total, \
            donor_avg))
    print(mail)


def mail_file():
    """
    Hopefully, this makes directories and files on first run for the listed
    donors.  Hopefully
    """
    path = os.getcwd()
    for k in donors:
        current_donor = ""
        current_donor = k
        donor_math = donors[current_donor]
        donor_total = sum(donor_math)
        donor_avg = len(donor_math)
        directory = path + '/donors/' + current_donor + '/'
        filename = current_donor + ' - ' \
        + datetime.datetime.now().strftime("%s") + ".txt"

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + filename, 'w+') as outfile:
            mail = ("Hello {}, \n"
                    "\n"
                    "We are writing to thank you for you generous donation\n"
                    "to our foundation.  Your contributions for the year \n"
                    "total ${:,.2f} in {} disbursements. \n"
                    "\n"
                    "Again, the foundation thanks you for your support, \n"
                    "and we hope to remain in contact with you in this new \n"
                    "year.\n"
                    "\n"
                    "Sincerely, \n"
                    "Ecumenical Slobs LLC \n".format(current_donor, \
                    donor_total, donor_avg))

            outfile.write("{}\n".format(mail))
    print("\nFiles created\n")


menu_choice = {"report": report,
               "send": donor_mail,
               "all": mail_file,
               "list": donor_list,
               "quit": goodbye
               }

def main():
    '''
    The man menu and the calls to other functions
    '''
    response = ""
    while True:
        while response not in VALID_INPUT:
            response = input(PROMPT)
        menu_choice[response]()
        response = input(PROMPT)

if __name__ == "__main__":
    main()
