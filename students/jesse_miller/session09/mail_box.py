#!/usr/bin/env python3
'''
This is the command interface for the mailroom.  Now that I know that donor
manipulations work correctly (At least according to pytest.  I mean, I wrote
the tests so the likelihood of human error here is high, you know?).
'''
#import os
import datetime
from donor_models import DonorCollection
#pylint: disable=C0103
alms = DonorCollection()
'''
Module imports
'''
class MailBox:
    '''
    Sending mail and directory writing functions
    '''
    @staticmethod
    def letter_template(donor, total, count):
        '''
        This is the template for the mail to write to screen and file
        '''
        date = datetime.datetime.now().strftime("%B %d, %Y")
        template = f'{date} \n'\
        f'\nHello {donor}, \n' \
        f'\n'\
        f'We are writing to thank you for you generous donation\n'\
        f'to our foundation.  Your contributions for the year \n'\
        f'total ${total} in {count} disbursements.'\
        f'\n'\
        f'\n'\
        f'Again, the foundation thanks you for your support, \n'\
        f'and we hope to remain in contact with you in this new \n'\
        f'year.\n'\
        f'\n'\
        f'Sincerely, \n'\
        f'Ecumenical Slobs LLC \n'
        return template


    @staticmethod
    def mail_send(donor):
        '''
        This function now contains both the singular and the all mails.  I am
        planning on rewriting it to print to terminal and mail for single or
        all.
        '''
        donor_math = alms.donors_dict[donor]
        print(MailBox.letter_template(donor, (sum(donor_math)), \
        (len(donor_math))))
