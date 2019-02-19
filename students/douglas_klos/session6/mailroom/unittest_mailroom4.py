#!/usr/bin/env python3
""" Mailroom v4 unittest assertions """

# Douglas Klos
# February 19th, 2019
# Python 210, Session 6, Mailroom v4 test suite
# test_mailroom4.py

import unittest
import mailroom4 as mr


class Mailroom4Test(unittest.TestCase):
    """ Test assertsion for mailroom4 using unittest """

    def test_send_thank_you(self):
        """ Test assertions for send_thank_you """

        assert(mr.send_thank_you_note('Maggie', 5000)
               == '\nDonation in the amount of 5000 from Maggie not found')
        assert(mr.send_thank_you_note('Mark', 5000)
               == '\nNo donation from Mark')
        assert(mr.send_thank_you_note('Maggie', 2222)
               == mr.THANK_YOU_NOTE.format('Maggie', 2222))

    def test_write_thank_you_files(self):
        """ Test assertions for write_thank_you_files """

        assert(mr.write_thank_you_files('/')
               == '\nPermission denied, / is not writeable')
        assert(mr.write_thank_you_files('/etc/')
               == '\nPermission denied, /etc/ is not writeable')
        assert(mr.write_thank_you_files('./thanks/')
               == '\nThank you files written to ./thanks/')

    def test_add_donor_to_database(self):
        """ Test assertions for add_donor_to_databse """

        assert(mr.add_donor_to_database('Douglas')
               == '\nDouglas is already present in database')
        assert('Douglas' in mr.mailroom_db.keys())

        assert(mr.add_donor_to_database('Paul')
               == '\nPaul has been added to database')
        assert('Paul' in mr.mailroom_db.keys())

        assert(mr.add_donor_to_database('')
               == '\n is not a valid name')
        assert('' not in mr.mailroom_db.keys())

    def test_add_donation_to_donor(self):
        """ Test assertions for add_donation_to_donor """

        assert(mr.add_donation_to_donor('Douglas', 1000)
               == '\nDonation 1000 added to donor Douglas')
        assert(1000 in mr.mailroom_db['Douglas'])

        assert(mr.add_donation_to_donor('John', 1000)
               == '\nJohn not found in database')
        assert('John' not in mr.mailroom_db.keys())

        assert(mr.add_donation_to_donor('Douglas', 'bad_data')
               == '\nbad_data is not a valid donation amount')
        assert('bad_data' not in mr.mailroom_db['Douglas'])

        assert(mr.add_donation_to_donor('Douglas', -1000)
               == '\n-1000 is not a valid donation amount')
        assert(-1000 not in mr.mailroom_db['Douglas'])

    def test_remove_donor_from_database(self):
        """ Test assertions for remove_donor_from_database """

        assert(mr.remove_donor_from_database('Douglas')
               == '\nDouglas removed from database')
        assert('Douglas' not in mr.mailroom_db.keys())

        assert(mr.remove_donor_from_database('Peter')
               == '\nPeter not found in database')
        assert('Peter' not in mr.mailroom_db.keys())

    def test_remove_donation_from_donor(self):
        """ Test assertions for remove_donation_from_donor """

        assert(mr.remove_donation_from_donor('Peter', 1000)
               == '\nPeter not found in database')
        assert('Peter' not in mr.mailroom_db.keys())

        assert(mr.remove_donation_from_donor('Jo', 8814)
               == '\nDonation 8814 has been removed from donor Jo')
        assert(8814 not in mr.mailroom_db['Jo'])

        assert(mr.remove_donation_from_donor('Jo', 5000)
               == '\nDonation 5000 from donor Jo not found in database')
        assert(5000 not in mr.mailroom_db['Jo'])

        assert(mr.remove_donation_from_donor('Jo', 'foo')
               == '\nDonation foo from donor Jo not found in database')
        assert('foo' not in mr.mailroom_db['Jo'])
