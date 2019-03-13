#!/usr/bin/env python3
#pylint: disable=R1710
""" Mailroom OO DonorDB class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donordb.py

import os


class DonorDB():
    """
    DonorDB class

    Properties:
    <insert properties>
    """

    def __init__(self, donor=None):
        self._database = []
        if donor:
            self._database.append(donor)

    def __str__(self):
        return self.display_database()

    def __repr__(self):
        return self.display_database()

    def display_database(self):
        """ Displays the database """
        return_string = ''
        for donor in self.database:
            return_string += f'{donor.name:>24} : {donor.donations}\n'
        return return_string

    def add_donor(self, donor):
        """
        Add a donor to the database

        :param donor: Donor to be added to database
        """
        self._database.append(donor)

    def remove_donor(self, donor):
        """
        Remove a donor from the database

        :param donor: Donor to be removed from database
        """
        self._database.remove(donor)

    def display_report(self):
        """ Prints a report of donors and their donations """

        report = '\n' + "-" * 79 + '\n'
        report += 'Donor Name\t\t|           Total Given | Num Gifts |      Average Gift\n'
        report += "-" * 79 + '\n'

        for donor in self.database:
            if donor.donations == []:
                report += (f'{donor.name:24s}\t\t         {len(donor.donations):10}\n')
            else:
                report += (f'{donor.name:24s}   '
                           f'$ {donor.total_donations:18,.2f}  '
                           f'{len(donor.donations):10}    '
                           f'$ {donor.total_donations/len(donor.donations):14,.2f}\n')

        report += "-" * 79 + '\n'

        return report

    def thank_you_files(self, path='./thanks/'):
        """
        Write thank you files to ./<path>/donor <date>.txt for each donor

        :param path: Path where files are to be written. Defaults to './thanks/
        """
        # Create directory and parents if they do not exist
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            return f'\nPermission denied, {path} is not writeable'

        for donor in self.database:
            # No donations from donor, no thank you note needed
            if donor.donations == []:
                continue
            try:
                donor.write_thank_you_letter(path)
            except PermissionError:
                return f'Permission denied, {path} is not writeable'

        return f'\nThank you files written to {path}'

    @property
    def database(self):
        """ Gets the database """
        return self._database
