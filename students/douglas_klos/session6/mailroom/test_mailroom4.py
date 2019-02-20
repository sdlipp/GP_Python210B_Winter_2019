#!/usr/bin/env python3
""" Mailroom v4 assertions """

# Douglas Klos
# February 20th, 2019
# Python 210, Session 6, Mailroom v4 test suite
# test_mailroom4.py

import mailroom4 as mr


# Test cases for send_thank_you

def test_send_thank_you1():
    assert(mr.send_thank_you_note('Maggie', 5000)
           == '\nDonation in the amount of 5000 from Maggie not found')


def test_send_thank_you2():
    assert(mr.send_thank_you_note('Mark', 5000)
           == '\nNo donation from Mark')


def test_send_thank_you3():
    assert(mr.send_thank_you_note('Maggie', 2222)
           == mr.THANK_YOU_NOTE.format('Maggie', 2222))


# Test cases for writing thank you files

def test_write_thank_you_files1():
    assert(mr.write_thank_you_files('/')
           == '\nPermission denied, / is not writeable')


def test_write_thank_you_files2():
    # Don't run sudo, not that you would...
    assert(mr.write_thank_you_files('/etc/')
           == '\nPermission denied, /etc/ is not writeable')


def test_write_thank_you_files3():
    assert(mr.write_thank_you_files('./thanks/')
           == '\nThank you files written to ./thanks/')


# Test cases for add_donor_to_database

def test_add_donor_to_database1():
    assert(mr.add_donor_to_database('Douglas')
           == '\nDouglas is already present in database')
    assert('Douglas' in mr.mailroom_db.keys())


def test_add_donor_to_database2():
    assert(mr.add_donor_to_database('Paul')
           == '\nPaul has been added to database')
    assert('Paul' in mr.mailroom_db.keys())


def test_add_donor_to_database3():
    assert(mr.add_donor_to_database('')
           == '\n is not a valid name')
    assert('' not in mr.mailroom_db.keys())


# Test cases for add_donation_to_donor

def test_add_donation_to_donor1():
    assert(mr.add_donation_to_donor('Douglas', 1000)
           == '\nDonation 1000 added to donor Douglas')
    assert(1000 in mr.mailroom_db['Douglas'])


def test_add_donation_to_donor2():
    assert(mr.add_donation_to_donor('John', 1000)
           == '\nJohn not found in database')
    assert('John' not in mr.mailroom_db.keys())


def test_add_donation_to_donor3():
    assert(mr.add_donation_to_donor('Douglas', 'bad_data')
           == '\nbad_data is not a valid donation amount')
    assert('bad_data' not in mr.mailroom_db['Douglas'])


def test_add_donation_to_donor4():
    assert(mr.add_donation_to_donor('Douglas', -1000)
           == '\n-1000 is not a valid donation amount')
    assert(-1000 not in mr.mailroom_db['Douglas'])


# Test cases for remove_donor_from_databse

def test_remove_donor_from_database1():
    assert(mr.remove_donor_from_database('Douglas')
           == '\nDouglas removed from database')
    assert('Douglas' not in mr.mailroom_db.keys())


def test_remove_donor_from_database2():
    assert(mr.remove_donor_from_database('Peter')
           == '\nPeter not found in database')
    assert('Peter' not in mr.mailroom_db.keys())


# Test cases for remove_donation_from_donor

def test_remove_donation_from_donor1():
    assert(mr.remove_donation_from_donor('Peter', 1000)
           == '\nPeter not found in database')
    assert('Peter' not in mr.mailroom_db.keys())


def test_remove_donation_from_donor2():
    assert(mr.remove_donation_from_donor('Jo', 8814)
           == '\nDonation 8814 has been removed from donor Jo')
    assert(8814 not in mr.mailroom_db['Jo'])


def test_remove_donation_from_donor3():
    assert(mr.remove_donation_from_donor('Jo', 5000)
           == '\nDonation 5000 from donor Jo not found in database')
    assert(5000 not in mr.mailroom_db['Jo'])


def test_remove_donation_from_donor4():
    assert(mr.remove_donation_from_donor('Jo', 'foo')
           == '\nDonation foo from donor Jo not found in database')
    assert('foo' not in mr.mailroom_db['Jo'])
