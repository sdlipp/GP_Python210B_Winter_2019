#!/usr/bin/env python3
'''
This is the command interface for the mailroom.  Now that I know that donor
manipulations work correctly (At least according to pytest.  I mean, I wrote
the tests so the likelihood of human error here is high, you know?).
'''
#import os
import sys
#import datetime
from donor_models import DonorCollection, Donor
'''
Module imports
'''

#pylint: disable=C0103
alms = DonorCollection()
'''
Because my sense of humor is odd, that's why.  Also setting an object
'''
prompt = '\n'.join(('Welcome to mailroom 1.0!',
                    '',
                    'Please choose from below options:',
                    'list   - Display a list of donors.',
                    'report - Display a report of donation totals.',
                    'send   - Generate letters to send to donors.',
                    'add    - Add a donor',
                    'delete - Remove a donor',
                    'quit   - Exit.',
                    '>>> '))

valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete', 'add')


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
    print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
    .format(headers[0], headers[1], headers[2], headers[3]))

    donor_data = alms.create_report()
    for row in donor_data:
        print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format\
        (row[0], row[1], row[2], row[3]))
    print(f"{'-'*80}\n")


def donor_mail_choice():
    '''
    This section allows the user to mail a donor
    '''
    current_donor = ''
    list_donors()
    try:
        current_donor = str(input('Who would you like to mail (all for all): '))
        if current_donor in alms.donors_dict:
            mail_send(current_donor)
        elif current_donor == 'all':
            mail_send(current_donor)
        else:
            donor_add(current_donor)
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()


def mail_send(current_donor):
    '''
    This function now contains both the singular and the all mails.  I am
    planning on rewriting it to print to terminal and mail for single or all.
    '''
#    path = os.getcwd()
#    name = ''
#    if name in alms.donors_dict:
#        directory = path + '/donors/' + current_donor + '/'
#        filename = name + ' - ' \
#            + datetime.datetime.now().strftime('%s') + '.txt'
#        Donor.letter_template(current_donor)
#        print('\nFile created\n')
#
#    else:
#        for k in alms.donors_dict:
#            name = k
#            directory = path + '/donors/' + current_donor + '/'
#            filename = name + ' - ' \
#                + datetime.datetime.now().strftime('%s') + '.txt'
#            Donor.letter_template(current_donor)
#        print('\nFiles created\n')
    while True:
        if current_donor in alms.donors_dict:
            print(Donor.letter_template(current_donor))
        if current_donor == 'all':
            for donor in alms.donors_dict:
                print(Donor.letter_template(current_donor))


def donor_add():
    '''
    Create a new donor if none exists
    '''
    current_donor = str(input('Enter the name of the new donor: '))
    alms.donor_creation(current_donor)
    list_donors()
    donor = alms.find_donor(current_donor)
    while True:
        try:
            d_num = int(input('How many donations were made: '))
            while d_num > 0:
                new_donation = float(input('Enter their donation: '))
                d_num -= 1
                donor.donation_add(new_donation)
            break
        except (KeyboardInterrupt, EOFError, ValueError):
            break


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


def donor_del():
    '''
    This section allows the user to delete a donor
    '''
    try:
        list_donors()
        del_donor = str(input('Enter the name of the donor to remove: '))
        del alms.donors_dict[del_donor]
        list_donors()
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()


menu_choice = {'report': print_report,
               'list': list_donors,
               'send': donor_mail_choice,
               'delete': donor_del,
               'add': donor_add,
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
