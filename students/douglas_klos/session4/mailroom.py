#!/usr/bin/env python3
""" Mailroom V2.1, now with more file writing and dictionaries! """

# Douglas Klos
# February 4th, 2019
# Python 210, Session 4, Mailroom v2.1
# mailroom.py

import os
import datetime

mailroom_db = {'Douglas': [5000, 2000],
               'Maggie': [2222, 3333, 4444],
               'Light Yagami': [124, 8975],
               'Makise Kurisu': [235987],
               'Youjo Senki': [13498.00, 9876, 1234],
               'Motoko Kusanagi': [57892, 239857, 87265],
               'Jo': [8814, 2320]}

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Send a Thank You\n'
               '2: Write thank you files\n'
               '3: Create a report\n'
               '4: Add a new donor to database\n'
               '5: Add a new donation to donor\n'
               '6: Remove donor from database\n'
               'p: Print database\n'
               'q: Quit\n'
               '>>> ')

THANK_YOU_PROMPT = ('\nPlease enter one of the following:\n'
                    '<Name>: Name of person to send a thank you note to\n'
                    'list: Display donors in the database\n'
                    'q: Return to main menu\n'
                    '>>> ')

THANK_YOU_NOTE = ('\nDear {}:\n'
                  '\tThank you for your very kind donation of ${:,.2f}.\n'
                  '\tIt will be put to very good use.\n'
                  '\t\tSincerely,\n'
                  '\t\t\tThe Team')

THANK_YOU_LETTER = ('Dear {}:\n'
                    '\tThank you for your most recenet donation of ${:,.2f}.\n'
                    '\tYour total generosity towards us is ${:,.2f}.\n'
                    '\tIt will be put to very good use.\n'
                    '\t\tSincerely,\n'
                    '\t\t\tThe Team\n')


def display_database():
    """ Displays all donors and their donations """

    print()

    for key in mailroom_db:
        print(f'{key:>24} : {mailroom_db[key]:}')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t\t| Num Gifts | Average Gift")
    print("-" * 79)
    for key in mailroom_db:
        if mailroom_db[key] == []:
            print(f'{key:24s}\t\t       {len(mailroom_db[key]):10}')
        else:
            print(f'{key:24s} '
                  f'$ {sum(mailroom_db[key]):16,.2f}    '
                  f'{len(mailroom_db[key]):10}    '
                  f'$ {sum(mailroom_db[key])/len(mailroom_db[key]):16,.2f}')


def add_donor(name_input=''):
    """ Adds name_input to the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter new donor's name: ")
        if name_input in mailroom_db.keys():
            print('Already exists')
            name_input = ''
        if name_input in ('q', 'Q'):
            return

    mailroom_db[name_input] = []


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit'):
            return
        if name not in mailroom_db.keys():
            print('Donor not found, please select from list')
        else:
            break

    while True:
        try:
            donation_input = input('Please enter a donation: ')
            if float(donation_input) < 0:
                print('Donation must be a positive number')
            else:
                mailroom_db[name].append(float(donation_input))
                break
        except ValueError:
            print(f'{donation_input} is not a valid entry')


def remove_donor(name_input=''):
    """ Remove donor from the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter new donor's name: ")
        if name_input in ('q', 'Q'):
            return
        if name_input in mailroom_db.keys():
            del mailroom_db[name_input]
        else:
            print(f'Donor {name_input} not found')


def thank_you_menu():
    """ Menu for Thank You options """

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        elif name_input.lower() in('l', 'list'):
            display_database()
            continue
        elif name_input in '':
            pass
        if name_input not in mailroom_db.keys():
            add_donor(name_input)
            print(f'\nAdding {name_input} to the database')
        else:
            send_thank_you(name_input)


def send_thank_you(name_input):
    """ Send thank you to donor for selected donation """

    if mailroom_db[name_input] == []:
        print(f'No donation from {name_input}')
        return

    print(f'Donation amounts for {name_input}: {mailroom_db[name_input]}')

    # All this try if else except is for error checking input
    while True:
        try:
            donation_input = float(input('Enter donation: '))
            if donation_input in mailroom_db[name_input]:
                print(THANK_YOU_NOTE.format(name_input, donation_input))
                return
            else:
                print(f'Donation from {name_input} '
                      f'in the amount of {donation_input} '
                      f'not found')
        except ValueError:
            print(f'Donation amountisfor {name_input}:'
                  f'{mailroom_db[name_input]}')


def write_thank_you_files():
    """ Write thank you files to ./thank_you_files/donor.txt for each donor """

    # Current datetime to append to filename
    now = datetime.datetime.now()

    # Get path from user for file writing
    path = input('Enter path for thank you files or blank for default: ')

    # If path left blank, set to default
    if path == '':
        path = "./thank_you_notes/"

    # Make sure there's a trailing slash on path
    elif path[-1] != '/':
        path += '/'

    # Create directory and parents if they do not exist
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except PermissionError:
        print(f'Permission denied, {path} is not writeable')
        return

    for donor in mailroom_db:
        filename = path + donor + ' ' + now.strftime("%Y-%m-%d %H:%M") + ".txt"

        # No donations from donor, no thank you note needed
        if mailroom_db[donor] == []:
            continue

        # Open file for writing
        try:
            with open(filename, 'w') as donor_file:
                donor_file.write(
                    THANK_YOU_LETTER.format(
                        donor,
                        mailroom_db[donor][len(mailroom_db[donor])-1],
                        sum(mailroom_db[donor])))
        except PermissionError:
            print(f'Permission denied, {path} is not writeable')
            return

    print(f'\nDonor letters written to {path}')


def main():
    """ Mailroom main function """

    menu = {'1': thank_you_menu,
            '2': write_thank_you_files,
            '3': create_report,
            '4': add_donor,
            '5': add_donation,
            '6': remove_donor,
            'p': display_database}

    selection = input(MAIN_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            menu[selection]()
        else:
            print('Invalid Input')

        selection = input(MAIN_PROMPT)


if __name__ == '__main__':
    main()
