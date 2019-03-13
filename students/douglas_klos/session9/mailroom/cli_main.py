#!/usr/bin/env python3
#pylint: disable=C0103, R1710
""" Mailroom OO User Interface """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# cli_main.py


from donor import Donor
from donorcollection import DonorCollection as DC


mailroom_db = DC()


def initialize_donors():
    donor1 = Donor('Douglas', 5000, 2000)
    donor2 = Donor('Maggie', 2222, 3333, 4444)
    donor3 = Donor('Light Yagami', 124, 8975)
    donor4 = Donor('Makise Kurisu', 235987)
    donor5 = Donor('Youjo Senki', 13498.00, 9876, 1234)
    donor6 = Donor('Motoko Kusanagi', 57892, 239857, 87265)
    donor7 = Donor('Jo', 8814, 2320)
    donor8 = Donor('Mark')

    mailroom_db.add_donor(donor1)
    mailroom_db.add_donor(donor2)
    mailroom_db.add_donor(donor3)
    mailroom_db.add_donor(donor4)
    mailroom_db.add_donor(donor5)
    mailroom_db.add_donor(donor6)
    mailroom_db.add_donor(donor7)
    mailroom_db.add_donor(donor8)


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


def display_menu(menu, value_type, prompt):
    selection = get_value(prompt, value_type)

    while selection.lower() not in ('q', 'quit'):
        if selection in menu.keys():
            # This would end up printing 'None' when calling 'q' or 'quit'
            # Don't know why, in the mean time we'll just error trap it.
            # print(menu[selection]())
            output = menu[selection]()
            if output:
                print(output)
        else:
            print('Invalid Input')
        selection = get_value(prompt, value_type)


def add_remove_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': add_donation,
            '2': remove_donation,
            '3': add_donor,
            '4': remove_donor,
            'p': display_database}

    ADD_REMOVE_PROMPT = ('\n1: Add donation\n'
                         '2: Remove donation\n'
                         '3: Add donor\n'
                         '4: Remove donor\n'
                         'p: Print database\n'
                         'q: Return to main menu\n'
                         '>>> ')

    display_menu(menu, str, ADD_REMOVE_PROMPT)


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
        return f'\n{donation} is not a valid donation amount'

    if donation < 0:
        return f'\n{donation} is not a valid donation amount'

    for donor in mailroom_db.collections:
        if donor.name == name:
            donor.add_donation(donation)
            return f'\nDonation {donation} has been added to donor {name}'
    return f'{name} not found in database'


def remove_donation():
    """ Prompts user for donation amount and donor to remove """

    display_database()
    name = get_value("Please enter name of donor: ", str)

    if name.lower() in ('q', 'quit'):
        return

    donation = get_value("Please enter donation amount: ", float)

    for donor in mailroom_db.collections:
        if donor.name == name:
            donor.remove_donation(donation)
            return f'\nDonation {donation} has been remove from donor {name}'
    return f'\nDonation {donation} from donor {name} not found in database'


def add_donor():
    """ Prompts user for name to enter into database """

    name = get_value("Please enter new donor's name: ", str)

    if name.lower() in ('q', 'quit'):
        return

    if name == '':
        return f'\n{name} is not a valid name'

    donor = Donor(name)
    mailroom_db.add_donor(donor)

    return f'Donor {name} has been added to the database'


def remove_donor():
    """ Prompts user for name to remove from database """

    name = get_value("Please enter name of donor to remove: ", str)

    if name.lower() in ('q', 'quit'):
        return

    for donor in mailroom_db.collections:
        if donor.name == name:
            mailroom_db.collections.remove(donor)
            return f'\n{name} removed from database'
    return f'{name} not found in database'


def thank_you_menu():
    menu = {'1': thank_you_note,
            '2': thank_you_files,
            'p': display_database}

    thank_you_prompt = ('\n1: Send a thank you note to a donor\n'
                        '2: Write thank you files for each donor\n'
                        'p: Display donors in the database\n'
                        'q: Return to main menu\n'
                        '>>> ')

    display_menu(menu, str, thank_you_prompt)


def thank_you_note():
    """ Send thank you to donor for selected donation """
    display_database()
    name = get_value('Please enter a donors name: ', str)

    for donor in mailroom_db.collections:
        if donor.name == name:
            return donor.display_thank_you_letter()
    return f'\nDonor {name} not found.'


def thank_you_files():
    """ Write thank you files to ./<path>/donor <date>.txt for each donor """

    # Get path from user for file writing
    path = input('Enter path for thank you files or blank for default (./thanks/): ')

    # If path left blank, set to default
    if path == '':
        path = "./thanks/"
    # Make sure there's a trailing slash on path
    elif path[-1] != '/':
        path += '/'

    print(mailroom_db.thank_you_files(path))


def display_report():
    return mailroom_db.display_report()


def display_database():
    print(mailroom_db)


def main():
    initialize_donors()
    display_database()

    menu = {'1': add_remove_menu,
            '2': thank_you_menu,
            '3': display_report,
            'p': display_database}

    main_prompt = ('\nWelcome to the Mail Room\n'
                   'Please choose from the following options:\n'
                   '1: Add or Remove a Donor or Donation\n'
                   '2: Send a thank you\n'
                   '3: Create report\n'
                   'p: Print database\n'
                   'q: Quit\n'
                   '>>> ')

    display_menu(menu, str, main_prompt)


if __name__ == '__main__':
    main()
