#!/usr/bin/env python3
""" Mailroom OO User Interface """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# cli_main.py


from donor import Donor
from donorcollection import DonorCollection as DC


mailroom_db = DC()

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Add or Remove a Donor or Donation\n'
               '2: Send a thank you\n'
               '3: Create report\n'
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


def initialize_donors():
    d1 = Donor('Douglas', 5000, 2000)
    d2 = Donor('Maggie', 2222, 3333, 4444)
    d3 = Donor('Light Yagami', 124, 8975)
    d4 = Donor('Makise Kurisu', 235987)
    d5 = Donor('Youjo Senki', 13498.00, 9876, 1234)
    d6 = Donor('Motoko Kusanagi', 57892, 239857, 87265)
    d7 = Donor('Jo', 8814, 2320)
    d8 = Donor('Mark')

    mailroom_db.add_donor(d1)
    mailroom_db.add_donor(d2)
    mailroom_db.add_donor(d3)
    mailroom_db.add_donor(d4)
    mailroom_db.add_donor(d5)
    mailroom_db.add_donor(d6)
    mailroom_db.add_donor(d7)
    mailroom_db.add_donor(d8)


def get_value(text, check_type, valid_inputs=None):
    """ Gets a value from the user of specified type """

    while True:
        try:
            value = check_type(input(text))
        except ValueError:
            print("Invalid value. Please try again")
            continue
        else:
            if valid_inputs:
                if value not in valid_inputs:
                    print(f"Valid inputs are {valid_inputs}. Please try again")
                    continue
            return value


def add_remove_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': add_donation,
            '2': remove_donation,
            '3': add_donor,
            '4': remove_donor,
            'p': display_database}

    selection = input(ADD_REMOVE_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            print(menu[selection]())
        else:
            print('Invalid Input')

        selection = input(ADD_REMOVE_PROMPT)


def add_donation():
    """ Prompts user for donor name and donation amount to add """

    display_database()

    name = get_value("Please enter name of donor: ", str)

    if name.lower() in ('q', 'quit'):
        return

    donation = get_value("Please enter donation amount: ", float)

    try:
        float(donation)
    except ValueError:
        return(f'\n{donation} is not a valid donation amount')

    if donation < 0:
        return(f'\n{donation} is not a valid donation amount')

    for donor in mailroom_db.collection:
        if donor.name == name:
            donor.add_donation(donation)
            return(f'\nDonation {donation} has been added to donor {name}')
    else:
        return(f'{name} not found in database')


def remove_donation():
    """ Prompts user for donation amount and donor to remove """

    display_database()

    name = get_value("Please enter name of donor: ", str)

    if name.lower() in ('q', 'quit'):
        return

    donation = get_value("Please enter donation amount: ", float)

    for donor in mailroom_db.collection:
        if donor.name == name:
            donor.remove_donation(donation)
            return(f'\nDonation {donation} has been remove from donor {name}')
    else:
        print(f'\nDonation {donation} from donor {name} not found in database')


def add_donor():
    """ Prompts user for name to enter into database """

    name = get_value("Please enter new donor's name: ", str)

    if name.lower() in ('q', 'quit'):
        return

    if name == '':
        return(f'\n{name} is not a valid name')

    donor = Donor(name)
    mailroom_db.add_donor(donor)

    return(f'Donor {name} has been added to the database')


def remove_donor():
    """ Prompts user for name to remove from database """

    name = get_value("Please enter name of donor to remove: ", str)

    if name.lower() in ('q', 'quit'):
        return

    for donor in mailroom_db.collection:
        if donor.name == name:
            mailroom_db.collection.remove(donor)
            return(f'\n{name} removed from database')
    else:
        return(f'{name} not found in database')


def thank_you_menu():
    pass


def display_report():
    pass


def display_database():
    print(mailroom_db)


def main():
    initialize_donors()
    display_database()

    menu = {'1': add_remove_menu,
            '2': thank_you_menu,
            '3': display_report,
            'p': display_database}

    selection = get_value(MAIN_PROMPT, str)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            menu[selection]()
        else:
            print('Invalid Input')

        selection = get_value(MAIN_PROMPT, str)


if __name__ == '__main__':
    main()
