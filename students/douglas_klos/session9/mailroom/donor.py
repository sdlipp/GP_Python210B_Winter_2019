#!/usr/bin/env python3
#pylint: disable=R1710, C0321, W1113
""" Mailroom OO Donor class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donor.py

import datetime


class Donor():
    """
    Donor class

    Attributes:
        name (string):    The name of the donor
        donations (list): The donations for the donor
    """

    THANK_YOU_LETTER = ('Dear {}:\n'
                        '\tThank you for your most recenet donation of ${:,.2f}.\n'
                        '\tYour total generosity towards us is ${:,.2f}.\n'
                        '\tIt will be put to very good use.\n'
                        '\t\tSincerely,\n'
                        '\t\t\tThe Team\n')

    def __init__(self, name='', *args):
        """
        Donor class initializer

        :param name: The name of the donor being created
        :param args: The initial donations for the donor
        """
        self._name = name
        self._donations = [value for value in args]

    def __str__(self):
        return f'{self.name} : {self.donations}'

    def __repr__(self):
        return f'{self.name} : {self.donations}'

    def add_donation(self, donation):
        """
        Adds a new donations to the donor.

        :param donation: The new donation to be added
        """
        self._donations.append(donation)

    def remove_donation(self, donation):
        """
        Removes a donation from the donor.

        :param donation: The donation to be removed
        """
        if donation in self.donations:
            self._donations.remove(donation)
            return f'Donation {donation} has been removed from {self.name}'
        else:
            return f'Donation {donation} not found for {self.name}'

    def display_thank_you_letter(self):
        """ Displays formatted thank you letter """
        if self.total_donations > 0:
            return self.THANK_YOU_LETTER.format(self.name, self.donations[-1], self.total_donations)
        return 'No donations found for donor'

    def write_thank_you_letter(self, path):
        """
        Writes thank you letter to the specified path

        :param path: Path to write thank you letter to
        """
        now = datetime.datetime.now()
        if path == '': path = './thanks/'
        if path[-1] != '/': path += '/'
        filename = path + self.name + ' ' + now.strftime("%Y-%m-%d") + ".txt"

        try:
            with open(filename, 'w') as donor_file:
                donor_file.write(self.THANK_YOU_LETTER.format(self.name,
                                                              self.donations[-1],
                                                              self.total_donations))
        except PermissionError:
            raise PermissionError

        return f'Thank you letter for {self.name} has been written to {filename}'

    @property
    def name(self):
        """ Sets or returns the donor's name """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def donations(self):
        """ Returns the donations list """
        return self._donations

    @property
    def total_donations(self):
        """ Returns the total amount of donations """
        return sum(self.donations)

    @property
    def average_donation(self):
        """ Returns the average amount of donations """
        if self.donations == []:
            return 0
        return sum(self.donations) / len(self.donations)
