#!/usr/bin/env python3
'''
This is the command interface for the mailroom.  Now that I know that donor
manipulations work correctly (At least according to pytest.  I mean, I wrote
the tests so the likelihood of human error here is high, you know?).
'''
#import os
import sys
#import datetime
from donor_models import DonorCollection
'''
Module imports
'''

#pylint: disable=C0103
alms = DonorCollection()
'''
Because my sense of humor is odd, that's why.  Also setting an object
'''

prompt = '\n'.join(('Welcome to mailroom 0.5!',
                    '',
                    'Please choose from below options:',
                    'report - If you would like a report of donations \
                    totals.',
                    'send - If you would like to send a thank you.',
                    'list - If you would like to see a list of donors.',
                    'delete - Remove a donor',
                    'quit   - Exit.',
                    '>>> '))

valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete')


def list_donors():
    """
    Lists existing donors.
    """
    print(f"\n{'-'*15}\nList of Donors:\n{'-'*15}")
    current = alms.list_donor()
    for donor in current:
        print(donor)
    print(f"{'-'*15}\n")


def print_report():
    """
    Prints a summary report of all donors.
    """
    headers = ["Donor Name", "Total Given", "Times Donated", "Average Gift"]
    print()
    print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
    .format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)

    donor_data = alms.create_report()

    for row in donor_data:
        #print("{:17} |  ${:>18,.2f} | {:>15} |  ${:>17,.2f}".format(row[0], \
        #row[1], row[2], row[3]))
        print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format \
              (row[0], row[1], row[2], row[3]))
        print(f"{'-'*80}\n")

def safe_input():
    '''
    This will be for handling keyboard exceptions
    '''
    return None


def goodbye():
    '''
    Gracefully exits
    '''
    print('Goodbye!')
    sys.exit()


menu_choice = {'report': print_report,
               'list': list_donors,
               'send': None,
               'delete': None,
               'quit': goodbye
              }


def main():
    '''
    The main menu and the calls to other functions.
    '''
    while True:
        try:
            response = input(prompt)
        except (KeyboardInterrupt, EOFError):
            continue
        if response not in valid_input:
            print('\nERROR: Invalid option')
            continue
        menu_choice[response]()
