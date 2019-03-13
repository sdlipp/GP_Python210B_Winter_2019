#!/usr/bin/env python3
'''
Let's try this by following the directions.  So, this is going to be where the
donor manipulation occurs.  The goal is to compartmentalize everything so that
functions can be called by other programs if and when needed.
'''
import datetime


class Donor:
    '''
    This will be slightly easier in a sense because we're only dealing with a
    single donor.  However, I get to look forward to pairing everything down to
    an interesting, if not insane, degree from previous attempts.
    '''

    def __init__(self, name):
        self.name = name
        self.donations = [] #?  We'll try it.


    def donation_add(self, new_donation):
        '''
        This should append donations to the list
        '''
        self.donations.append(new_donation)

    @property
    def donation_count(self):
        '''
        Fairly obvious, counts the number of donations
        '''
        return len(self.donations)

    @property
    def donation_total(self):
        '''
        Again, obvious, adds the donations up
        '''
        return sum(self.donations)

    @property
    def donation_average(self):
        '''
        Averages the donations
        '''
        return self.donation_total / self.donation_count


    def letter_template(self):
        '''
        I'm a tad worried about the linting error, but we'll give it a shot
        '''
        date = datetime.datetime.now().strftime("%B %d, %Y")
        template = f'\n {date} \n'\
        f'\nHello {self.name}, \n' \
        f'\n'\
        f'We are writing to thank you for you generous donation\n'\
        f'to our foundation.  Your contributions for the year \n'\
        f'total ${self.donations:,.2f} in {self.donation_average} disbursements.'\
        f'\n'\
        f'\n'\
        f'Again, the foundation thanks you for your support, \n'\
        f'and we hope to remain in contact with you in this new \n'\
        f'year.\n'\
        f'\n'\
        f'Sincerely, \n'\
        f'Ecumenical Slobs LLC \n'
        return template


#class DonorCollection:
