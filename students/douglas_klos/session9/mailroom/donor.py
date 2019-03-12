#!/usr/bin/env python3
""" Mailroom OO Donor class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donor.py


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

    def add_donation(self, donation):
        """
        Adds a new donations to the donor.

        :param donation: The new donation to be added
        """
        self._donations.append(donation)

    def remove_donation(self, donation):    
        self._donations.remove(donation)

    def display_thank_you_letter(self):
        """ Displays formatted thank you letter """
        return self.THANK_YOU_LETTER.format(self.name, self.donations[-1], self.total_donations)

    def write_thank_you_letter(self, path):
        """
        Writes thank you letter to the specified path

        :param path: Path to write thank you letter to
        """
        filename = f'{path}/{self.name}.txt' if path[-1] != '/' else f'{path}{self.name}.txt'
        with open(filename, 'w') as donor_file:
            donor_file.write(self.THANK_YOU_LETTER.format(self.name,
                                                          self.donations[-1],
                                                          self.total_donations))

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
        """ Sets or returns donations """
        return self._donations

    @property
    def total_donations(self):
        """ Returns the total amount of donations for the Donor """
        return sum(self._donations)
