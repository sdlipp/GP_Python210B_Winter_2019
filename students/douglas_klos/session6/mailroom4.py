#!/usr/bin/env python3
""" Mailroom V4.0, now refactored with more testing! """

# Douglas Klos
# February 16th, 2019
# Python 210, Session 6, Mailroom v4
# mailroom4.py

import os
import datetime

mailroom_db = {'Douglas': [5000, 2000],
               'Maggie': [2222, 3333, 4444],
               'Light Yagami': [124, 8975],
               'Makise Kurisu': [235987],
               'Youjo Senki': [13498.00, 9876, 1234],
               'Motoko Kusanagi': [57892, 239857, 87265],
               'Jo': [8814, 2320],
               'Mark': []}

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Send a Thank You\n'
               '2: Write thank you files\n'
               '3: Create a report\n'
               '4: Add or Remove a Donor or Donation\n'
               'p: Print database\n'
               'q: Quit\n'
               '>>> ')

ADD_REMOVE_PROMPT = ('\n1: Add donation\n'
                     '2: Remove donation\n'
                     '3: Add donor\n'
                     '4: Remove donor\n'
                     'p: Print database\n'
                     'q: Return to main menu\n'
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


# The following functions have been refactored to facilitate testing
# add_donor_input
# add_donor_to_database
# add_donation_input
# add_donation_to_donor
# remove_donor_input
# remove_donor_from_database
# remove_donation_input
# remove_donation_from_donor

def add_donor_input():
    """ Prompts user for name to enter into database """

    name_input = ''

    while name_input in '':
        name_input = input("Please enter new donor's name: ")

        if name_input.lower() in ('q', 'quit'):
            return
    
    print(add_donor_to_database(name_input))
    # mailroom_db[name_input] = []
    

def add_donor_to_database(donor):
    """ Add input name to database """

    if donor == '':
        return(f'\n{donor} is not a valid name')

    if donor in mailroom_db.keys():
        return(f'\n{donor} is already present in database')

    mailroom_db[donor] = []
    return (f'\n{donor} has been added to database')


def remove_donor_input():
    """ Prompts user for name to remove from database """

    name_input = ''

    while name_input in '':
        name_input = input("Please enter donor's name to remove: ")
        
        if name_input.lower() in ('q', 'quit'):
            return

    # del mailroom_db[name_input]
    print(remove_donor_from_database(name_input))
    

def remove_donor_from_database(donor):
    """ Removes donor from database """

    if donor not in mailroom_db.keys():
        return(f'\n{donor} not found in database')
    
    del mailroom_db[donor]
    return(f'\n{donor} removed from database')
    

def add_donation_input():
    """ Prompts user for donor name and donation amount to add """

    display_database()

    while True:
        name_input = input('\nPlease select a donor to add a donation to: ')
        if name_input.lower() in ('q', 'quit'):
            return
        else:
            break
        
    while True:
        try:
            donation_input = abs(float(input('Please enter a donation: ')))
        except ValueError:
            print(f'Donation must be a positive number')
        else:
            break

    print(add_donation_to_donor(name_input, donation_input))


def add_donation_to_donor(donor, donation):
    """ Add donation to specified donor """
    
    if donor not in mailroom_db.keys():
        return(f'\n{donor} not found in database')
    
    try:
        float(donation)
    except ValueError:
        return(f'\n{donation} is not a valid donation amount')

    if donation < 0:
        return(f'\n{donation} is not a valid donation amount')
    
    mailroom_db[donor].append(donation)
    return(f'\nDonation {donation} added to donor {donor}')


def remove_donation_input():
    """ Promptos user for donation amount and donor to remove """

    display_database()

    while True:
        name_input = input("Please enter donor's name to remove: ")
        if name_input.lower() in ('q', 'quit'):
            return        
        else:
            break

    while True:
        try:
            donation_input = float(
                             input("Please enter donation name to remove: "))
        except ValueError:
            print(f'Invalid Entry')
        else:
            break

    print(remove_donation_from_donor(name_input, donation_input))
            

def remove_donation_from_donor(donor, donation):
    """ Remove donation from donor """

    if donor not in mailroom_db.keys():
        return(f'\n{donor} not found in database')

    for donations in mailroom_db[donor]:
        if donation == donations:
            mailroom_db[donor].remove(donation)
            return(f'\nDonation {donation} has been removed from donor {donor}')
    
    return(f'\nDonation {donation} from donor {donor} not found in database')
 

def add_remove_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': add_donation_input,
            '2': remove_donation_input,
            '3': add_donor_input,
            '4': remove_donor_input,
            'p': display_database}

    selection = input(ADD_REMOVE_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            menu[selection]()
        else:
            print('Invalid Input')

        selection = input(ADD_REMOVE_PROMPT)


def thank_you_menu():
    """ Menu for Thank You options """

    display_database()

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        elif name_input.lower() in ('l', 'list'):
            display_database()
            continue
        elif name_input in '':
            pass
        elif name_input not in mailroom_db.keys():
            print(add_donor_to_database(name_input))
        elif mailroom_db[name_input] == []:
            print(f'No donations from {name_input}')
        else:
            break

    while True:
        try:
            donation_input = float(input('Enter donation: '))
        except ValueError:
            print(f'\nInvalid donation entered')
        else:
            if donation_input in mailroom_db[name_input]:
                print(send_thank_you_note(name_input, donation_input))
                return
            else:
                print(f'Donation from {name_input} in the amount of {donation_input} not found')
            

def send_thank_you_note(donor, donation):
    """ Send thank you to donor for selected donation """

    if mailroom_db[donor] == []:
        return(f'\nNo donation from {donor}')
        
    if donation in mailroom_db[donor]:
        return(THANK_YOU_NOTE.format(donor, donation))

    return(f'\nDonation in the amount of {donation} from {donor} not found')


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
            '4': add_remove_menu,
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