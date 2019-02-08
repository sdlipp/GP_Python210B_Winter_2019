#!/usr/bin/env python3
import sys

from operator import itemgetter
from collections import OrderedDict, defaultdict

DONORS = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}

prompt = "\n".join(("Welcome to my charity!",
          "Please select and option below:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))


def view_donor_names():

    for k,v in DONORS.items():
        print(k)


def add_new_donor(name, donor_list):

    amount = int(input(f'How much would this donor like to donate?'))
    donor_list[name] = [amount]


def write_a_letter(name, amount):
    letter = f'Dear {name},\n\nThank you for your kind donation of {amount:,.0f}\n\n'\
        f'Rest assured that these funds will be put to optimal use.\n\n' \
        f'Best regards,\n' \
        f'The Charitable Charities Team'
    return letter




def add_donations_and_send_thank_you():

    while True:

        answer = input('Please enter a donor Full Name.')

        if answer.lower() == 'list':
            view_donor_names()
            continue

        amount = int(input('How much would this donor like to donate?'))

        if answer not in DONORS:
            DONORS[answer] = [amount]

        else:
            for name, donations in DONORS.items():
                if name == answer:
                    donations.append(amount)

        print(f'\nThank you {answer.split()[0]} for you generous donation of ${amount:,.0f}\n')
        break


def create_new_donors_dict():
    '''
    dictionay comprehension of DONORS with sum, len, and average of values.
    '''
    new_donors = {k: (sum(v), len(v), (sum(v) / len(v))) for k, v in DONORS.items()}
    new_donors = OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))
    return new_donors


def create_report():

    header=f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}{"| Average Donation".rjust(20)}'
    print(header)
    print('-'*len(header))

    #get new donors dict from function
    for k,v in create_new_donors_dict().items():
        print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')

def quit_the_program():
    print('Tschüss')
    sys.exit()


def dictionary_switch(selection):
    '''
    Create the switch dictionary
    '''
    functions = {'1':add_donations_and_send_thank_you,
                 '2':create_report,
                 '3':quit_the_program}
    #defaultdict doesn't seem to work here
    functions = defaultdict(lambda: 'Please make a valid selection', functions)

    if selection in functions:
        return functions[selection]()
    else:
        print('Please make a valid selection', '\n')

def main():

    while True:
        write_a_letter('me', 123)
        # response = input(prompt)
        # dictionary_switch(response)


if __name__ == '__main__':
    main()

