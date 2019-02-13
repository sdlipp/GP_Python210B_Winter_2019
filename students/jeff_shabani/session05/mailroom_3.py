#!/usr/bin/env python3
import os
import sys

from collections import OrderedDict, defaultdict
from operator import itemgetter
from pathlib import Path

DONORS = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}

prompt = "\n".join(("Welcome to my charity!",
                    "Please select and option below:",
                    "1 - Send a Thank You to an individual",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>> "))


def view_donor_names():
    for name in DONORS:
        print(name)


def add_new_donor(name, donor_list):
    amount = int(input(f'How much would this donor like to donate?'))
    try:
        donor_list[name] = [amount]
    except ValueError:
        print('Please enter a valid numerical amount')
    else:donor_list[name] = [amount]


def write_a_letter(name, amount):
    letter = f'Dear {name},\n\nThank you for your kind donation of ${amount:,.0f}\n\n' \
        f'Rest assured that these funds will be put to optimal use.\n\n' \
        f'Best regards,\n' \
        f'The Charitable Charities Team'
    return letter


def get_directory_for_letter():
    location = input(f'Please enter the full path of the directory\n'
                     f'where you want to save your letters.\n'
                     f'Hit <Enter> to save to the current working directory.')

    if location:
        save_path = Path(f'{location}')
        cd = os.chdir(save_path)
    else:
        cd = os.getcwd()
    return cd


def add_donations_and_send_thank_you():
    while True:

        answer = input('Please enter a donor Full Name.')

        if answer.lower() == 'list':
            view_donor_names()
            continue

        amount = int(input('How much would this donor like to donate?'))

        get_directory_for_letter()

        if answer not in DONORS:
            DONORS[answer] = [amount]
            with open(f'{answer}.txt', 'wt') as letter:
                letter.write(write_a_letter(answer, amount))


        else:
            for name, donations in DONORS.items():
                if name == answer:
                    donations.append(amount)
            with open(f'{answer}.txt', 'wt') as letter:
                letter.write(write_a_letter(answer, amount))

        print(f'\nThank you {answer.split()[0]} for you generous donation of ${amount:,.0f}\n')
        break


def create_new_donors_dict():
    """
    dictionay comprehension of DONORS with sum, len, and average of values.
    """
    new_donors = {k: (sum(v), len(v), (len(v) / len(v))) for k, v in DONORS.items()}
    new_donors = OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))
    return new_donors


def write_letters_to_all_donors():
    get_directory_for_letter()
    for donor, total in create_new_donors_dict().items():
        with open(f'{donor}.txt', 'wt') as letter:
            letter.write(write_a_letter(donor, total[0]))


def create_report():
    header = f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}' \
        f'{"| Average Donation".rjust(20)}'
    print(header)
    print('-' * len(header))

    # get donors and totals from new_donors dictionary
    for k, v in create_new_donors_dict().items():
        print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')


def quit_the_program():
    print('Tschüss')
    sys.exit()


def dictionary_switch(selection):
    """
    Create the switch dictionary. Tried a defaultdict here
    but it doesn't seem to work as a switch.
    """
    functions = {'1': add_donations_and_send_thank_you,
                 '2': create_report,
                 '3': write_letters_to_all_donors,
                 '4': quit_the_program}

    """
    try/except block to catch unvalid keys
    """
    try:
        return functions[selection]()
    except KeyError:
        print('Please make a valid selection', '\n')


def main():
    while True:
        response = input(prompt)
        dictionary_switch(response)


if __name__ == '__main__':
    main()
