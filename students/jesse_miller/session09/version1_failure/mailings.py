#!/usr/bin/env python3
'''
Mailing functions to send out donation thanks yous
'''
import datetime
import os
from donors import Donor, DonorListings
from menus import MailMenu


class MailSetup():
    '''
    This will be the mailing subsystem.  The plan is to capture data from
    donors to send out the mail files
    '''
    def __init__(self):
        self.total_dons = Donor.total_dons


    @property
    def auto_mailer(self):
        '''
        This will be our auto mailing function for sending thank yous to
        our donors
        '''
        letter = f'{datetime.datetime.now().strftime("%B %d, %Y")} \n, \n'\
                 f'\nHello {self.name}, \n'\
                 f'\n'\
                 f'We are writing to thank you for you generous donation\n'\
                 f'to our foundation.  Your contributions for the year \n'\
                 f'total ${self.total_dons}. \n'\
                 f'\n'\
                 f'Again, the foundation thanks you for your support, \n'\
                 f'and we hope to remain in contact with you in this new \n'\
                 f'year.\n'\
                 f'\n'\
                 f'Sincerely, \n'\
                 f'Ecumenical Slobs LLC \n'
        return letter


    def donor_mail_choice(self):
        '''
        This section allows the user to mail a donor
        '''
        self.name = ''
        #    self.name = DonorListings.donor_list(self)
        try:
            self.name = str(input('Who would you like to mail (all for all)\
            : '))
            if self.name in DonorListings.donor_list(self.name):
                mail_send(self.name)
            elif self.name == 'all':
                mail_send(self.name)
            else:
                DonorListings.donor_creation(self.name)
        except (KeyboardInterrupt, EOFError, ValueError):
            MailMenu.safe_input()


    def mail_send(self):
        '''
        This function now contains both the singular and the all mails.  I am
        planning on rewriting it to print to terminal and mail for single or all.
        '''
        path = os.getcwd()

        if self.name in DonorListings.donors_dict:
            donor_math = donors[self.name]
            directory = path + '/donors/' + self.name + '/'
            filename = self.name + ' - ' \
                + datetime.datetime.now().strftime('%s') + '.txt'
            mail_format(self.name, donor_math, directory, filename)
            print('\nFile created\n')
        else:
            for k in donors:
                self.name = k
                donor_math = donors[self.name]
                directory = path + '/donors/' + self.name + '/'
                filename = self.name + ' - ' \
                    + datetime.datetime.now().strftime('%s') + '.txt'
                mail_format(self.name, donor_math, directory, filename)
            print('\nFiles created\n')


    def mail_format(self, donor_math, directory, filename):
        '''
        This is the formating for the mail print and file.  This allows us to
        have both files and terminal output for single donors as well as multiple
        '''
        print('\n')
        print(letter.format(self.name, (sum(donor_math)), (len(donor_math))))

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + filename, 'w+') as outfile:
            outfile.write('{}\n'.format(letter.format(self.name,\
            (sum(donor_math)), (len(donor_math)))))
