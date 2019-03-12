#!/usr/bin/env python3
'''
The main menuing subsystem
'''
from os import sys
from donors import DonorListings
from mailings import MailSetup

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
    menu_choice = {'report': DonorListings.create_report,
                   'send': MailSetup.donor_mail_choice,
                   'list': DonorListings.donor_list,
                   'quit': goodbye
                  }
    valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete')
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

    while True:
        try:
            response = input(prompt)
        except (KeyboardInterrupt, EOFError):
            continue
        if response not in valid_input:
            print('\nERROR: Invalid option')
        continue
    menu_choice[response]()


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


def main():
    '''
    Here we go!
    '''
    print('Mailroom 1.0')
    MailMenu.main_menu(None)
