#!/usr/bin/env python3
#pylint: disable=R1710
""" Mailroom OO DonorCollection class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donorcollection.py


import os


class DonorCollection():
    """
    Donor Collection class

    Properties:
    <insert properties>
    """

    def __init__(self, donor=None):
        self._collections = []
        if donor:
            self._collections.append(donor)

    def add_donor(self, donor):
        self._collections.append(donor)

    def remove_donor(self, donor):
        self._collections.remove(donor)

    def display_collections(self):
        return_string = ''
        for donor in self.collections:
            return_string += f'{donor.name:>24} : {donor.donations}\n'
        return return_string

    def thank_you_files(self, path='./thanks/'):
        """ Write thank you files to ./<path>/donor <date>.txt for each donor """
        # Create directory and parents if they do not exist
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            return f'\nPermission denied, {path} is not writeable'

        for donor in self.collections:
            # No donations from donor, no thank you note needed
            if donor.donations == []:
                continue
            # filename = path + donor.name + ' ' + now.strftime("%Y-%m-%d") + ".txt"
            try:
                donor.write_thank_you_letter(path)
            except PermissionError:
                return f'Permission denied, {path} is not writeable'

        return f'\nThank you files written to {path}'

    def display_report(self):
        """ Prints a report of donors and their donations """

        report = '\n' + "-" * 79 + '\n'
        report += 'Donor Name\t\t|           Total Given | Num Gifts |      Average Gift\n'
        report += "-" * 79 + '\n'

        for donor in self.collections:
            if donor.donations == []:
                report += (f'{donor.name:24s}\t\t         {len(donor.donations):10}\n')
            else:
                report += (f'{donor.name:24s}   '
                           f'$ {donor.total_donations:18,.2f}  '
                           f'{len(donor.donations):10}    '
                           f'$ {donor.total_donations/len(donor.donations):14,.2f}\n')

        report += "-" * 79 + '\n'

        return report

    def __str__(self):
        return self.display_collections()

    def __repr__(self):
        return self.display_collections()

    @property
    def collections(self):
        """ Gets the collections object of objects """
        return self._collections
