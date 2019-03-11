#!/usr/bin/env python3

"""
Framework for individual donors.
"""

# Jeff Shabani
# March 1st, 2019
# Python 210, Session 9
# donors.py

class Donor():

    donors = {}
    donations = list()

    def __init__(self, name=''):
        self.name = name
        self.donation = []

    def add_donor(self, answer, amount):
        self.donations.append(amount)
        self.donors[answer] = self.donations





    donors_ex = {'William B': [120, 130, 50],
              'Sammy Maudlin': [500, 125, 670, 1000],
              'Bobby Bittman': [10],
              'Skip Bittman': [75, 125, 19],
              'Ashley Lashbrooke': [10000, 15000]}