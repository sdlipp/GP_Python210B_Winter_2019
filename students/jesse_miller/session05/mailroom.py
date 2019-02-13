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
                    "list - If you would like to see a list of donors.",
                    "quit   - Exit.",
                    ">>> "))

VALID_INPUT = ("report", "quit", "list", "send", "all")

MAIL = ("\nHello {}, \n"
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
        "Ecumenical Slobs LLC \n")


def safe_input():
    """
    This will be for handling keyboard exceptions
    """
    return None


def report():
    '''
    This will be the donation report section
    '''
    summary = []
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print("-"*80)
    print("{:17} | {:<20} | {:<15} | {:<19}".format(headers[0], headers[1],
                                                    headers[2], headers[3]))
    print("-"*80)

    for k, v in donors.items():
        summary.append([k, (sum(v)), (len(v)), (sum(v) / len(v))])
    summary.sort(key=lambda d: d[1], reverse=True)
    for x in summary:
        print("{:17} | ${:<18,.2f} | {:<15} |  ${:<17,.2f}".format(x[0], x[1],
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
    try:
        current_donor = str(input("Who would you like to mail (all for all): "))
        if current_donor in donors:
            print("")
        elif current_donor == 'all':
            mail_send(current_donor)
        else:
            donor_add(current_donor)
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()
    else:
        mail_send(current_donor)


def donor_add(current_donor):
    """
    This allows addition of new donors
    """
    if current_donor not in donors:
        donors[current_donor] = []
    while True:
        try:
            d_num = int(input("How many donations were made: "))
            while d_num > 0:
                new_don = float(input("Enter their donation: "))
                donors[current_donor].append(new_don)
                d_num -= 1
        except (KeyboardInterrupt, EOFError, ValueError):
            safe_input()
        else:
            return False
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
    This function now contains both the singular and the all mails.  I am
    planning on rewriting it to print to terminal and mail for single or all.
    """
    path = os.getcwd()

    if current_donor in donors:
        donor_math = donors[current_donor]
        print(MAIL.format(current_donor, (sum(donor_math)), (len(donor_math))))
    else:
        for k in donors:
            current_donor = k
            donor_math = donors[current_donor]
            directory = path + '/donors/' + current_donor + '/'
            filename = current_donor + ' - ' \
                + datetime.datetime.now().strftime("%s") + ".txt"

            print('\n')
            print(MAIL.format(current_donor, (sum(donor_math)),
                              (len(donor_math))))

            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(directory + filename, 'w+') as outfile:
                outfile.write("{}\n".format(MAIL.format(current_donor, \
                (sum(donor_math)), (len(donor_math)))))

        print("\nFiles created\n")


menu_choice = {"report": report,
               "send": donor_mail,
               "list": donor_list,
               "quit": goodbye
               }


def main():
    '''
    The man menu and the calls to other functions.  Interestingly, the
    exception only works on load.  Once a function is called, it crashes.
    '''
    response = ""
    while response not in VALID_INPUT:
        try:
            response = input(PROMPT)
        except (KeyboardInterrupt, EOFError):
            safe_input()
    menu_choice[response]()
    response = input(PROMPT)


if __name__ == "__main__":
    main()
