#!/usr/bin/env python3
'''
Mailing functions to send out donation thanks yous
'''
import datetime
from donors import Donor, DonorListings
from menus import MailMenu

class MailSetup():
    '''
    This will be the mailing subsystem.  The plan is to capture data from
    donors to send out the mail files
    '''
    def __init__(self):
        current_donor = ''
        self.name = current_donor
        self.total_dons = Donor.total_dons

    @staticmethod
    def auto_mailer():
        '''
        This will be our auto mailing function for sending thank yous to
        our donors
        '''
        letter = f'{datetime.datetime.now().strftime("%B %d, %Y")} \n, \n'\
                 f'\nHello {self.name}, \n'\
                 f'\n'\
                 f'We are writing to thank you for you generous donation\n'\
                 f'to our foundation.  Your contributions for the year \n'\
                 f'total ${self.total_dons[-1]:,.2f}. \n'\
                 f'\n'\
                 f'Again, the foundation thanks you for your support, \n'\
                 f'and we hope to remain in contact with you in this new \n'\
                 f'year.\n'\
                 f'\n'\
                 f'Sincerely, \n'\
                 f'Ecumenical Slobs LLC \n'
        return letter

    def donor_mail_choice():
        '''
        This section allows the user to mail a donor
        '''
        current_donor = ''
        #    current_donor = DonorListings.donor_list(self)
        try:
            current_donor = str(input('Who would you like to mail (all for all)\
            : '))
            if current_donor in DonorListings.donor_list(current_donor):
                mail_send(current_donor)
            elif current_donor == 'all':
                mail_send(current_donor)
            else:
                DonorListings.donor_creation(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            MailMenu.safe_input()
