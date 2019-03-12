#!/usr/bin/env python3
""" Mailroom OO Donor class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donor.py


class Donor():
    """
    Donor class

    Properties:
    <insert properties
    """

    def __init__(self, name, *args):
        self._name = name
        self._donations = [value for value in args]

    def add_donation(self, donation):
        self._donations.append(donation)

    def remove_donation(self, donation):    
        self._donations.remove(donation)

    @property
    def name(self):
        """ Sets or returns the name """
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



    # @donations.setter
    # def donations(self, value):
    #     self._donations.append(value)

    # @donations.deleter
    # def donations(self, value):
    #     print(value)
    #     del self._donations[value]
