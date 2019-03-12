#!/usr/bin/env python3
'''
Version 2, I think I was once again overthinking things, so now I'm going to
get what I had in the standalone working, then work on paring it down from
there rather than a complete rewrite
'''
from os import sys
from donorproc import DonorFunctions, DonorOutput
from mailsend import MailMethod

def main():
    '''
    Here we go!
    '''
    MainMenu.main()

class MainMenu:
    '''
    This will be the main menu, and the variable storage for menus displayed
    '''
    def __init__(self, name):
        self.name = name


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


    menu_choice = {'report': DonorOutput.donor_report,
                   'send': MainMenu.donor_mail_choice,
                   'list': DonorOutput.donor_list,
                   'delete': DonorFunctions.donor_del,
                   'quit': goodbye
                  }


    def donor_mail_choice(self):
        '''
        This section allows the user to mail a donor
        '''
        current_donor = ''
        DonorOutput.donor_list()
        try:
            current_donor = str(input('Who would you like to mail \
            (all for all): '))
            if current_donor in DonorFunctions.donors:
                MailMethod.mail_send(current_donor)
            elif current_donor == 'all':
                MailMethod.mail_send(current_donor)
            else:
                DonorFunctions.donor_add(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            MainMenu.safe_input(self)


    def safe_input(self):
        '''
        This will be for handling keyboard exceptions
        '''
        return None


    def goodbye(self):
        '''
        Gracefully exits
        '''
        print('Goodbye!')
        sys.exit()


    def main(self):
        '''
        The main menu and the calls to other functions.
        '''
        while True:
            try:
                response = input(MainMenu.prompt)
            except (KeyboardInterrupt, EOFError):
                continue
            if response not in MainMenu.valid_input:
                print('\nERROR: Invalid option')
                continue
            MainMenu.menu_choice[response]()
