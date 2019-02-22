#!/usr/bin/env python3
import unittest
from pathlib import Path

from students.jeff_shabani.session06 import mailroom_4

ANSWER = 'New_Donor'
AMOUNT = 4512


class mailroomTests(unittest.TestCase):

    def test_add_donor_to_donors(self):
        """
        tests that new donor is added to donors
        :return: int
        """
        self.assertEqual(mailroom_4.add_donor(ANSWER, AMOUNT), 6)

    def test_write_single_letter(self):
        """
        test that a single letter is written, saved as a text
        file and named correctly.
        :return: bool
        """
        self.assertEqual(mailroom_4.write_a_single_letter(ANSWER, AMOUNT), True)

    def test_view_donor_names(self):
        """
        test that function returns all donor names
        :return: str
        """
        self.assertEqual(mailroom_4.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke'))

    def test_letter_text(self):
        """
        tests that text in letter is correct
        :return:
        """
        letter_text = str()
        with open(f'{Path.cwd()}/{ANSWER}.txt') as infile:
            for line in infile:
                letter_text += line
        self.assertEqual(mailroom_4.write_a_letter(ANSWER, AMOUNT), letter_text)


if __name__ == '__main__':
    unittest.main()
