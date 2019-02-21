#!/usr/bin/env python3
import unittest
from pathlib import Path

from students.jeff_shabani.session06 import mailroom_4


class mailroomTests(unittest.TestCase):

    def test_add_donor_to_donors(self):
        """
        tests that new donor is added to donors
        :return: int
        """
        self.assertEqual(mailroom_4.add_donor('New_Donor', 4512), 6)

    def test_write_single_letter(self):
        """
        test that a single letter is written
        :return: bool
        """
        self.assertEqual(mailroom_4.write_a_single_letter('New_Donor', 4512), True)

    def test_view_donor_names(self):
        """
        test that function returns all donor names
        :return: str
        """
        self.assertEqual(mailroom_4.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke'))

    def test_letter_text(self):
        pass


if __name__ == '__main__':
    unittest.main()
