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

class MailRoom:
    '''
    All the calls and commands will be through this class.  Manipulation of
    donor information is done in donor_models.py, and all of the execution for
    this subprogram is from mailroom_oo.py
    '''
    @staticmethod
    def list_donors():
        """
        Lists existing donors.
        """
        print(f"\n{'-'*15}\nList of Donors:\n{'-'*15}")
        current = alms.list_donor()
        for donor in current:
            print(donor)
        print(f"{'-'*15}\n")

    @staticmethod
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


    @staticmethod
    def donor_mail_choice():
        '''
        This section allows the user to mail a donor
        '''
        current_donor = ''
        MailRoom.list_donors()
        try:
            donor = str(input('Who would you like to mail (all for all): '))
            if alms.find_donor(donor):
                MailRoom.mail_send_one(donor)
            if current_donor == 'all':
                MailRoom.mail_send_all()
        except (KeyboardInterrupt, EOFError, ValueError):
            MailRoom.safe_input()


    @staticmethod
    def mail_send_one(donor):
        '''
        This function now contains both the singular and the all mails.  I am
        planning on rewriting it to print to terminal and mail for single or all.
        '''
        print(Donor.letter_template(donor))


    @staticmethod
    def mail_send_all():
        '''
        This function now contains both the singular and the all mails.  I am
        planning on rewriting it to print to terminal and mail for single or all.
        '''
        pass
        #print(Donor.letter_template(donor))


    @staticmethod
    def safe_input():
        '''
        This will be for handling keyboard exceptions
        '''
        return None


    @staticmethod
    def goodbye():
        '''
        Gracefully exits
        '''
        print('Goodbye!')
        sys.exit()


    @staticmethod
    def donor_del():
        '''
        This section allows the user to delete a donor
        '''
        try:
            MailRoom.list_donors()
            del_donor = str(input('Enter the name of the donor to remove: '))
            del alms.donors_dict[del_donor]
            MailRoom.list_donors()
        except (KeyboardInterrupt, EOFError, ValueError):
            MailRoom.safe_input()

################################################################################
'''
End MailRoom
'''
################################################################################

class Menus(MailRoom):
    '''
    Menuing class, for those paying attention at home.  This is where the
    menu system resides, in case it needs tweeking.
    '''

    prompt = '\n'.join(('Welcome to mailroom 1.0!',
                        '',
                        'Please choose from below options:',
                        'list   - Display a list of donors.',
                        'report - Display a report of donation totals.',
                        'send   - Generate letters to send to donors.',
                        'delete - Remove a donor',
                        'quit   - Exit.',
                        '>>> '))

    valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete', 'add')


    menu_choice = {'report': MailRoom.print_report,
                   'list': MailRoom.list_donors,
                   'send': MailRoom.donor_mail_choice,
                   'delete': MailRoom.donor_del,
                   'quit': MailRoom.goodbye
                  }

    @staticmethod
    def main():
        '''
        The main menu and the calls to other functions.
        '''
        while True:
            try:
                response = input(Menus.prompt)
            except (KeyboardInterrupt, EOFError):
                continue
            if response not in Menus.valid_input:
                print('\nERROR: Invalid option')
                continue
            Menus.menu_choice[response]()

################################################################################
'''
End Menus
'''
################################################################################
