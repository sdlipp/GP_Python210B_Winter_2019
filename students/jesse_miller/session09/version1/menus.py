#!/usr/bin/env python3
'''
The main menuing subsystem
'''
from os import sys
from donors import DonorListings, Donor
from mailings import MailSetup

def main():
    '''
    Here we go!
    '''
    MailMenu.main_menu(None)


class MailMenu():
    '''
    Setting up the class for the menu
    '''
    def __init__(self, name):
        self.name = name


    def main_menu(self):
        '''
        The main menu
        '''
    menu_choice = {'report': DonorListings.donor_report,
                   'send': MailSetup.donor_mail_choice,
                   'list': DonorListings.donor_list,
                   'delete': donor_del,
                   'quit': goodbye
                  }
    valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete')
    prompt = '\n'.join(('Welcome to mailroom 1.0!',
                        '',
                        'Please choose from below options:',
                        'report - If you would like a report of donations \
                        totals.',
                        'send - If you would like to send a thank you.',
                        'list - If you would like to see a list of donors.',
                        'delete - Remove a donor',
                        'quit   - Exit.',
                        '>>> '))

    while True:
        try:
            response = input(prompt)
        except (KeyboardInterrupt, EOFError):
            continue
        if response not in valid_input:
            print('\nERROR: Invalid option')
        continue
    menu_choice[response]()


    def donor_mail_choice():
        '''
        This section allows the user to mail a donor
        '''
        current_donor = ''
        DonorListings.donor_list()
        try:
            current_donor = str(input('Who would you like to mail (all for all)\
            : '))
            if current_donor in donors:
                mail_send(current_donor)
            elif current_donor == 'all':
                mail_send(current_donor)
            else:
                donor_add(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            safe_input()


    @staticmethod
    def goodbye():
        '''
        Gracefully exits
        '''
        print('Goodbye!')
        sys.exit()


    @staticmethod
    def safe_input():
        '''
        This will be for handling keyboard exceptions
        '''
        return None


    @property
    def donor_del(self):
        '''
        This section allows the user to delete a donor
        '''
        try:
            DonorListings.donor_list(self)
            del_donor = str(input('Enter the name of the donor to remove: '))
            DonorListings.donor_delete(self, del_donor)
            DonorListings.donor_list(self)
        except (KeyboardInterrupt, EOFError, ValueError):
            MailMenu.safe_input()
