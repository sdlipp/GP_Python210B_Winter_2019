#!/usr/bin/env python3
#pylint: disable=R1710
""" Mailroom OO DonorDB class """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# donordb.py

import os
import pickle
from io import StringIO
from donor import Donor
import html_render as hr


class DonorDB():
    """
    DonorDB class

    Attributes:
        database: Data structure containing donors
    """

    def __init__(self, donor=None):
        self._database = {}
        if donor:
            self._database[donor.name] = donor

    def __str__(self):
        return self.display_database()

    def __repr__(self):
        return self.display_database()

    def display_database(self):
        """ Displays the database """
        return_string = ''
        for key in self.database:
            return_string += f'{self.database[key].name:>24} : {self.database[key].donations}\n'
        return return_string

    def add_donor(self, donor):
        """
        Add a donor to the database

        :param donor: Donor to be added to database. Donor objects will be added directly,
                          names will be added as donor objects with no donations.
        """
        if isinstance(donor, Donor):
            self.database[donor.name] = donor
        elif donor in self.database.keys():
            return f'{donor} already exists in database'
        else:
            self.database[donor] = Donor(donor)

        return f'{donor} has been added to the database'

    def add_donation(self, donor, donation):
        """
        Add a donation to the database

        :param donor: Name of donor to add donation to
        :param donation: Donation to be added to donor
        """
        try:
            float(donation)
        except ValueError:
            return f'{donation} is not a valid donation amount'

        if donation <= 0:
            return f'{donation} is not a valid donation amount'

        try:
            self.database[donor].add_donation(donation)
            return f'Donation {donation} has been added to donor {donor}'
        except KeyError:
            return f'{donor} not found in database'

    def remove_donor(self, donor):
        """
        Remove a donor from the database

        :param donor: Donor to be removed from database
        """
        try:
            del self.database[donor]
            return f'{donor} removed from database'
        except KeyError:
            return f'{donor} not found in database'

    def remove_donation(self, donor, donation):
        """
        Remove a donation from the database

        :param donor: Name of donor to remove donation from
        :param donation: Donation to be added to the database
        """
        try:
            return self.database[donor].remove_donation(donation)
        except KeyError:
            return f'Donation {donation} from donor {donor} not found in database'

    def display_report(self):
        """ Prints a report of donors and their donations """
        report = '\n' + "-" * 79 + '\n'
        report += 'Donor Name\t\t|           Total Given | Num Gifts |      Average Gift\n'
        report += "-" * 79 + '\n'

        for key in self.database:
            if self.database[key].donations == []:
                report += f'{self.database[key].name:24s}\t\t\t\t  0\n'
            else:
                report += (f'{self.database[key].name:24s}   '
                           f'$ {self.database[key].total_donations:18,.2f}  '
                           f'{len(self.database[key].donations):10}    '
                           f'$ {self.database[key].average_donation:14,.2f}\n')

        report += "-" * 79 + '\n'

        return report

    def html_report(self):
        """ Saves a report in HTML format """

        rendered_page = StringIO()

        page = hr.Html()
        head = hr.Head()
        head.append(hr.Meta(charset="UTF-8"))
        head.append(hr.Title("Mailroom OO Report"))
        page.append(head)
        body = hr.Body()
        body.append(hr.H(2, "Donation Report"))

        table = hr.Table(border=1)
        table.append(hr.Th('Name'))
        table.append(hr.Th('Total Given'))
        table.append(hr.Th('Number of Gifts'))
        table.append(hr.Th('Average Gift'))

        for key in self.database:
            table_row = hr.Tr()
            if self.database[key].donations == []:
                table_row.append(hr.Td(f'{self.database[key].name}'))
                table_row.append(hr.Td('0'))
                table_row.append(hr.Td('0'))
                table_row.append(hr.Td('0'))
                table.append(table_row)
            else:
                table_row.append(hr.Td(f'{self.database[key].name}'))
                table_row.append(hr.Td(f'${self.database[key].total_donations}'))
                table_row.append(hr.Td(f'{len(self.database[key].donations)}'))
                table_row.append(hr.Td(f'${self.database[key].average_donation}'))
                table.append(table_row)

        body.append(table)
        page.append(body)
        page.render(rendered_page, '    ')
        with open('./mailroom.html', 'w') as outfile:
            outfile.write(rendered_page.getvalue())
        return f'HTML report saved to ./mailroom.html'

    def thank_you_note(self, donor):
        """
        Returns a thank you note for the specified donor

        :param donor: Name of the donor to send the letter to
        """
        try:
            return self.database[donor].display_thank_you_letter()
        except KeyError:
            return f'Donor {donor} not found.'

    def thank_you_files(self, path):
        """
        Write thank you files to ./<path>/<donor> <date>.txt for each donor

        :param path: Path where files are to be written. Defaults to './thanks/
        """
        # Create directory and parents if they do not exist
        if path == '':
            path = './thanks/'
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            return f'Permission denied, {path} is not writeable'

        for key in self.database:
            # No donations from donor, no thank you note needed
            if self.database[key].donations == []:
                continue
            try:
                self.database[key].write_thank_you_letter(path)
            except PermissionError:
                return f'Permission denied, {path} is not writeable'

        return f'Thank you files written to {path}'

    def save_db_to_disk(self, filename='./mailroom_db.pkl'):
        """
        Save database to disk using pickle

        :param filename: Filename to be written to the disk
        """
        with open(filename, 'wb') as file:
            pickle.dump(self._database, file)
        return f'Database has been pickled to {filename}'

    def read_db_from_disk(self, filename='./mailroom_db.pkl'):
        """
        Load database from disk using pickle

        :param filename: Filename to be read from disk
        """
        try:
            with open(filename, 'rb') as file:
                self._database = pickle.load(file)
            return f'Database restored from pickle {filename}'
        except FileNotFoundError:
            raise FileNotFoundError

    def rename_donor(self, name, new_name):
        """
        Renames a donor

        :param name: Donor to be renamed
        :param new_name: New name for donor
        """
        try:
            self.database[new_name] = self.database[name]
            self.database[new_name].name = new_name
            del self.database[name]
        except KeyError:
            return f'{name} not found in database'

    @property
    def database(self):
        """ Gets the database """
        return self._database
