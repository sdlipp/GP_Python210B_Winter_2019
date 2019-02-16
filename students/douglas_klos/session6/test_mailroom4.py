#!/usr/bin/env python3
""" Mailroom v4 assertions """

# Douglas Klos
# February 16th, 2019
# Python 210, Session 6, Mailroom v4 test suite
# test_mailroom4.py

from mailroom4 import *

# Test cases for add_donor_to_database

def test_add_donor_to_database_1():
    assert add_donor_to_database('Douglas') == '\nDouglas is already present in database'
    assert 'Douglas' in mailroom_db.keys()


def test_add_donor_to_database_2():
    assert add_donor_to_database('Paul') == '\nPaul has been added to database'
    assert 'Paul' in mailroom_db.keys()


def test_add_donor_to_database_3():
    assert add_donor_to_database('') == '\n is not a valid name'
    assert '' not in mailroom_db.keys()


# Test cases for add_donation_to_donor

def test_add_donation_to_donor_1():
    assert add_donation_to_donor('Douglas', 1000) == '\nDonation 1000 added to donor Douglas'
    assert 1000 in mailroom_db['Douglas']
    

def test_add_donation_to_donor_2():
    assert add_donation_to_donor('John', 1000) == '\nJohn not found in database'
    assert 'John' not in mailroom_db.keys()


def test_add_donation_to_donor_3():
    assert add_donation_to_donor('Douglas', 'bad_data') == '\nbad_data is not a valid donation amount'
    assert 'bad_data' not in mailroom_db['Douglas']


def test_add_donation_to_donor_4():
    assert add_donation_to_donor('Douglas', -1000) == '\n-1000 is not a valid donation amount'
    assert -1000 not in mailroom_db['Douglas']


# Test cases for remove_donor_from_databse

def test_remove_donor_from_database_1():
    assert remove_donor_from_database('Douglas') == '\nDouglas removed from database'
    assert 'Douglas' not in mailroom_db.keys()


def test_remove_donor_from_database_2():
    assert remove_donor_from_database('Peter') == '\nPeter not found in database'
    assert 'Peter' not in mailroom_db.keys()


# Test cases for remove_donation_from_donor

def test_remove_donation_from_donor_1():
    assert remove_donation_from_donor('Peter', 1000) == '\nPeter not found in database'
    assert 'Peter' not in mailroom_db.keys()
    pass
    

def test_remove_donation_from_donor_2():
    assert remove_donation_from_donor('Jo', 8814) == '\nDonation 8814 has been removed from donor Jo'
    assert 8814 not in mailroom_db['Jo']
    pass


def test_remove_donation_from_donor_3():
    assert remove_donation_from_donor('Jo', 5000) == '\nDonation 5000 from donor Jo not found in database'
    assert 5000 not in mailroom_db['Jo']
    pass
    

def test_remove_donation_from_donor_4():
    assert remove_donation_from_donor('Jo', 'foo') == '\nDonation foo from donor Jo not found in database'
    assert 'foo' not in mailroom_db['Jo']
    pass