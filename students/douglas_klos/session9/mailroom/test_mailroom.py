#!/usr/bin/env python3
#pylint: disable=C0103
""" Mailroom OO pytest """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# test_mailroom.py


import os
import shutil
import datetime
import pytest
from donor import Donor
from donordb import DonorDB as db


#--------------------------------------------------------------------------------------------------#
#                                          donor.py tests
#--------------------------------------------------------------------------------------------------#


def test_init():
    """ Test initialization of donor objects """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor()

    assert d1.name == 'Maggie'
    assert d2.name == 'Doug'
    assert 1000 in d2.donations
    assert d3.name == ''

    d3.name = 'Sam'
    assert d3.name == 'Sam'


def test_add_donation():
    """ Test ability to add donations to donor """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor()

    d1.add_donation(1000)
    d2.add_donation(2000)
    d2.add_donation(3000)
    d3.add_donation(5000)

    assert 1000 in d1.donations
    assert 1000 in d2.donations
    assert 2000 in d2.donations
    assert 3000 in d2.donations
    assert 2000 not in d1.donations
    assert 5000 in d3.donations


def test_remove_donation():
    """ Test ability to remove donations from donor """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)

    d1.remove_donation(1000)
    d1.remove_donation(2000)
    d2.remove_donation(5555)
    d2.remove_donation(1111)

    assert 3000 in d1.donations
    assert 1000 not in d1.donations
    assert 2000 not in d1.donations
    assert 1111 not in d2.donations
    assert 5555 not in d2.donations

    message = d1.remove_donation(1337)
    assert message == f'Donation 1337 not found for donor {d1.name}'


def test_total_donations():
    """ Test total_donations property """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.total_donations == 6000
    d1.add_donation(4000)
    assert d1.total_donations == 10000
    d1.remove_donation(1000)
    assert d1.total_donations == 9000


def test_average_donation():
    """ Test average_donation property """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.average_donation == 2000
    d1.add_donation(4000)
    assert d1.average_donation == 2500
    d1.remove_donation(1000)
    assert d1.average_donation == 3000


def test_change_donor_name():
    """ Test ability to change donors name. """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.name == 'Maggie'
    d1.name = 'Doug'
    assert d1.name == 'Doug'


def test_thank_you_letter():
    """ Test that thank you letters are displayed properly """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug')
    letter1 = d1.display_thank_you_letter()
    print(letter1)
    assert d1.THANK_YOU_LETTER.format(d1.name, d1.donations[-1], d1.total_donations) == letter1
    letter2 = d2.display_thank_you_letter()
    assert letter2 == 'No donations found for donor'


def test_write_thank_you_letter():
    """ Test that a thank you letter is written to the disk containing the correct information """
    now = datetime.datetime.now()
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d1.write_thank_you_letter('.')
    assert os.path.isfile('Maggie ' + now.strftime("%Y-%m-%d") + ".txt")

    with open('./Maggie ' + now.strftime("%Y-%m-%d") + ".txt") as filename:
        contents = filename.read()
        total_donations = f'{d1.total_donations:,.2f}'
        most_recent = f'{d1.donations[-1]:,.2f}'
        assert d1.name in contents
        assert total_donations in contents
        assert most_recent in contents

    os.remove('./Maggie ' + now.strftime("%Y-%m-%d") + ".txt")

    with pytest.raises(PermissionError):
        d1.write_thank_you_letter('/')


def test_donor_str():
    """ Tests donor __str__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert str(d1) == 'Maggie : [1000, 2000, 3000]'


def test_donor_repr():
    """ Tests donor __repr__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert repr(d1) == 'Maggie : [1000, 2000, 3000]'


#--------------------------------------------------------------------------------------------------#
#                                          donordb.py tests
#--------------------------------------------------------------------------------------------------#


def test_init_donordb():
    """ Tests ability to initialze a databse of multiple donor objects """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor('ｷﾗ', 9001)

    db1 = db(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)

    assert d1 in db1.database
    assert d2 in db1.database
    assert d3 in db1.database


def test_donordb_str():
    """ Tests donordb __str__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    string = f'{d1.name:>24} : {d1.donations}\n'
    string += f'{d2.name:>24} : {d2.donations}\n'
    string += f'{d3.name:>24} : {d3.donations}\n'

    assert str(db1) == string


def test_donordb_repr():
    """ Tests donordb __repr__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    string = f'{d1.name:>24} : {d1.donations}\n'
    string += f'{d2.name:>24} : {d2.donations}\n'
    string += f'{d3.name:>24} : {d3.donations}\n'

    assert repr(db1) == string


def test_remove_donor():
    """ Tests ability to remove a donor from donordb """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    db1.remove_donor(d2)

    assert d1 in db1.database
    assert d2 not in db1.database
    assert d3 in db1.database


def test_display_report():
    """ Tests that reports contain the correct information """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)

    report = db1.display_report()

    assert d1.name in report
    assert d2.name in report
    assert d3.name in report
    assert f'{d1.total_donations:,.2f}' in report
    assert f'{d2.total_donations:,.2f}' in report
    assert f'{d3.total_donations:,.2f}' in report
    assert f'{d1.average_donation:,.2f}' in report
    assert f'{d2.average_donation:,.2f}' in report
    assert f'{d3.average_donation:,.2f}' in report


def test_thank_you_files():
    """ Tests that donordb writes the correct thank you files """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)

    db1.thank_you_files()
    file_count = len([name for name in os.listdir('./thanks/')])
    assert file_count == 2
    shutil.rmtree('./thanks/')

    assert db1.thank_you_files('/') == f'Permission denied, / is not writeable'
    assert db1.thank_you_files('/etc/nope') == f'\nPermission denied, /etc/nope is not writeable'


def test_save_db_to_disk():
    """ Tests that you can save the database to disk """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)

    db1.save_db_to_disk('./test_db.pkl')
    assert os.path.isfile('./test_db.pkl')
    os.remove('./test_db.pkl')


def test_read_db_from_disk():
    """ Tests that database can be loaded from disk """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    db2 = db()

    db1.save_db_to_disk('./test_db.pkl')
    db2.read_db_from_disk('./test_db.pkl')

    assert str(d1) in str(db2.database)
    assert str(d2) in str(db2.database)
    assert str(d3) in str(db2.database)

    os.remove('./test_db.pkl')
