#!/usr/bin/env python3

import unittest
import mailroom4

class MailroomTest(unittest.TestCase):

    def test_write_a_letter(self):
        donor = 'donor'
        amount = 200
        self.assertEqual(mailroom4.write_a_letter(donor, amount), True)


    def test_add_donor(self):
        new_donor = 'new_donor'
        self.assertEqual(mailroom4.add_donor(new_donor), True)

    def test_view_donor_names(self):
        self.assertEqual(mailroom4.view_donor_names(),
                         print('\nJeff Bezos\nPaul Allen\nElon Musk\nMark Zuckerberg'))

    def test_get_letter_text(self):
        donor = 'donor'
        letter_text = str()
        with open(f'{donor}.txt', 'wt') as letter:
            for line in letter:
                letter_text += line
        self.assertEqual(mailroom4.write_a_letter(), letter_text)

    def test_report(self):
        self.assertEqual(mailroom4.report(), True)


if __name__ == '__main__':
    unittest.main()