#!/usr/bin/env python3
""" Mailroom OO DonorCollection class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donorcollection.py


from donor import Donor


class DonorCollection():
    """
    Donor Collection class

    Properties:
    <insert properties>
    """

    def __init__(self, donor=None):
        self._collection = []
        if donor:
            self._collection.append(donor)

    def add_donor(self, donor):
        self._collection.append(donor)

    def remove_donor(self, donor):
        self._collection.remove(donor)

    def display_collection(self):
        return_string = ''
        for donor in self.collection:
            return_string += f'{donor.name:>24} : {donor.donations}\n'
        return return_string

    def __str__(self):
        return self.display_collection()

    def __repr__(self):
        return self.display_collection()

    @property
    def collection(self):
        """ Gets the collection object of objects """
        return self._collection
