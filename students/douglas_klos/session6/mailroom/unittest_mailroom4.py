#!/usr/bin/env python3
""" Mailroom v4 unittest assertions """

# Douglas Klos
# February 20th, 2019
# Python 210, Session 6, Mailroom v4 test suite
# test_mailroom4.py

import unittest
import mailroom4 as mr


class Mailroom4Test(unittest.TestCase):
    """ Test assertsion for mailroom4 using unittest """

    def test_send_thank_you(self):
        """ Test assertions for send_thank_you """

        self.assertEqual(mr.send_thank_you_note('Maggie', 5000),
                         '\nDonation in the amount of 5000 from Maggie not found')
        self.assertEqual(mr.send_thank_you_note('Mark', 5000),
                         '\nNo donation from Mark')
        self.assertEqual(mr.send_thank_you_note('Maggie', 2222),
                         mr.THANK_YOU_NOTE.format('Maggie', 2222))

    def test_write_thank_you_files(self):
        """ Test assertions for write_thank_you_files """

        self.assertEqual(mr.write_thank_you_files('/'),
                         '\nPermission denied, / is not writeable')
        self.assertEqual(mr.write_thank_you_files('/etc/'),
                         '\nPermission denied, /etc/ is not writeable')
        self.assertEqual(mr.write_thank_you_files('./thanks/'),
                         '\nThank you files written to ./thanks/')

    def test_add_donor_to_database(self):
        """ Test assertions for add_donor_to_databse """

        self.assertEqual(mr.add_donor_to_database('Douglas'),
                         '\nDouglas is already present in database')
        self.assertIn('Douglas', mr.mailroom_db.keys())

        self.assertEqual(mr.add_donor_to_database('Paul'),
                         '\nPaul has been added to database')
        self.assertIn('Paul', mr.mailroom_db.keys())

        self.assertEqual(mr.add_donor_to_database(''),
                         '\n is not a valid name')
        self.assertNotIn('', mr.mailroom_db.keys())

    def test_add_donation_to_donor(self):
        """ Test assertions for add_donation_to_donor """

        self.assertEqual(mr.add_donation_to_donor('Douglas', 1000),
                         '\nDonation 1000 added to donor Douglas')
        self.assertIn(1000, mr.mailroom_db['Douglas'])

        self.assertEqual(mr.add_donation_to_donor('John', 1000),
                         '\nJohn not found in database')
        self.assertNotIn('John', mr.mailroom_db.keys())

        self.assertEqual(mr.add_donation_to_donor('Douglas', 'bad_data'),
                         '\nbad_data is not a valid donation amount')
        self.assertNotIn('bad_data', mr.mailroom_db['Douglas'])

        self.assertEqual(mr.add_donation_to_donor('Douglas', -1000),
                         '\n-1000 is not a valid donation amount')
        self.assertNotIn(-1000, mr.mailroom_db['Douglas'])

    def test_remove_donor_from_database(self):
        """ Test assertions for remove_donor_from_database """

        self.assertEqual(mr.remove_donor_from_database('Douglas'),
                         '\nDouglas removed from database')
        self.assertNotIn('Douglas', mr.mailroom_db.keys())

        self.assertEqual(mr.remove_donor_from_database('Peter'),
                         '\nPeter not found in database')
        self.assertNotIn('Peter', mr.mailroom_db.keys())

    def test_remove_donation_from_donor(self):
        """ Test assertions for remove_donation_from_donor """

        self.assertEqual(mr.remove_donation_from_donor('Peter', 1000),
                         '\nPeter not found in database')
        self.assertNotIn('Peter', mr.mailroom_db.keys())

        self.assertEqual(mr.remove_donation_from_donor('Jo', 8814),
                         '\nDonation 8814 has been removed from donor Jo')
        self.assertNotIn(8814, mr.mailroom_db['Jo'])

        self.assertEqual(mr.remove_donation_from_donor('Jo', 5000),
                         '\nDonation 5000 from donor Jo not found in database')
        self.assertNotIn(5000, mr.mailroom_db['Jo'])

        self.assertEqual(mr.remove_donation_from_donor('Jo', 'foo'),
                         '\nDonation foo from donor Jo not found in database')
        self.assertNotIn('foo', mr.mailroom_db['Jo'])

if __name__ == '__main__':
    unittest.main()
