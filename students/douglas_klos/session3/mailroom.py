#!/usr/bin/env python3

# Douglas Klos
# February 1st, 2019
# Python 210
# mailroom.py, Mailroom v1.2

# There are more functions than requested in the assignment.
# I felt it needed a better way to add new donors than just through
# send_thank_you function, and a way to add new donations to current
# donors.  Note that you can add new donors through send_thank_you
# as requested in the assignment.


mailroom_db = [('Douglas', [5000, 2000]),
               ('Maggie', [2222, 3333, 4444]),
               ('Light Yagami', [124, 8975]),
               ('Makise Kurisu', [235987]),
               ('Youjo Senki', [13498.00, 9876, 1234]),
               ('Motoko Kusanagi', [57892, 239857, 87265]),
               ('Jo', [8814, 2320])]

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Send a Thank You\n'
               '2: Create a report\n'
               '3: Add a new donor\n'
               '4: Add a new donation\n'
               '5: Print database\n'
               'q: Quit\n'
               '>>> ')

THANK_YOU_PROMPT = ('\nPlease enter one of the following:\n'
                    '<Name>: Name of person to send a thank you note to\n'
                    'list: Display donors in the database\n'
                    'q: Return to main menu\n'
                    '>>> ')

THANK_YOU_NOTE = ('\nDear {}:\n'
                  '\tThank you for your very kind donation of ${:.2f}.\n'
                  '\tIt will be put to very good use.\n'
                  '\t\tSincerely\n'
                  '\t\t\tThe Team')


def get_new_donations():
    """ Queries user for donations """

    donations = []

    # Gets a float or integer input from user and adds to donations.
    # Started out with 'if not donation_input.isdigit()' but it
    # wouldn't deal with floats.  Try / Except was the only way I found
    # to process possible float values.  Further I didn't want trailing
    # or solitare 0's in the databse, such as 123.00, 123.0, 0, 0.0
    # and needed to handle erroneous inputs.
    while True:
        try:
            donation_input = float(input('Enter donation, 0 to quit: '))
            if donation_input < 0:
                print('Invalid input')
            elif donation_input == 0:
                break
            elif donation_input.is_integer():
                donations.append(int(donation_input))
            else:
                donations.append(donation_input)
        except ValueError:
            print('Invalid input')
    return donations


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit'):
            return
        elif not any(name in sub_list for sub_list in mailroom_db):
            print('Donor not found, please select from list')
        else:
            break

    donations = get_new_donations()

    # Find the name in the database and add new donations
    for donor, donation in mailroom_db:
        if donor == name:
            donation.extend(donations)


def add_donor(name_input):
    """ Adds name_input to the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter new donor's name: ")
        if any(name_input in sub_list for sub_list in mailroom_db):
            print('Already exists')
            name_input = ''
        if name_input in ('q', 'Q'):
            return
    donations = get_new_donations()

    mailroom_db.extend([(name_input, donations)])


def display_database():
    """ Displays all donors and their donations """

    print()
    for donor, donations in mailroom_db:
        print(f'{donor:>24} : {donations:}')


def thank_you_menu():
    """ Menu for Thank You options """

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        elif name_input.lower() in('l', 'list'):
            display_database()
        # We just want the menu again if a blank line is entered.
        elif name_input in '':
            pass
        # Check to see if the name entered exists in the database
        # If name not found, verify you want to add it.
        elif not any(name_input in sub_list for sub_list in mailroom_db):
            add_check = input('Donor not found, would you like to add?: ')
            if add_check.lower() in ('y', 'yes'):
                add_donor(name_input)

        # The name was found in the database
        else:
            send_thank_you(name_input)


def send_thank_you(name_input):
    """ Send thank you to donor for selected donation """

    for donor, donations in mailroom_db:
        if name_input == donor:
            print(f'Donation amounts for {donor}: {donations}')

            # All this try if else except is for error checking input
            print(donations)
            while True:
                try:
                    donation_input = float(input('Enter donation: '))
                    if donation_input in donations:
                        print(THANK_YOU_NOTE.format(donor, donation_input))
                        return
                    else:
                        print(f'Donation from {donor} '
                              f'in the amount of {donation_input} '
                              f'not found')
                except ValueError:
                    print('Invaild entry')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t\t| Num Gifts | Average Gift")
    print("-" * 79)
    for donor in mailroom_db:
        if donor[1] == []:
            print(f'{donor[0]:24s}\t\t       {len(donor[1]):10}')
        else:
            print(f'{donor[0]:24s} '
                  f'$ {sum(donor[1]):16,.2f}    '
                  f'{len(donor[1]):10}    '
                  f'$ {sum(donor[1])/len(donor[1]):16,.2f}')


def main():
    """ Mailroom main function """

    while True:
        selection = input(MAIN_PROMPT)
        if selection in '1':
            thank_you_menu()
        elif selection in '2':
            create_report()
        elif selection in '3':
            add_donor('')
        elif selection in '4':
            add_donation()
        elif selection in ('5', 'p', 'print'):
            display_database()
        elif selection.lower() in ('q', 'quit'):
            break
        else:
            print("Not a valid entry")


if __name__ == '__main__':
    main()
