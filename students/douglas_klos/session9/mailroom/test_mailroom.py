#!/usr/bin/env python3
""" Mailroom OO pytest """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# test_mailroom.py


import os
from donor import Donor
from donorcollection import DonorCollection as dc


def test_init():
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


def test_total_donations():
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.total_donations == 6000
    d1.add_donation(4000)
    assert d1.total_donations == 10000
    d1.remove_donation(1000)
    assert d1.total_donations == 9000


def test_change_donor_name():
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.name == 'Maggie'
    d1.name = 'Doug'
    assert d1.name == 'Doug'


def test_thank_you_letter():
    d1 = Donor('Maggie', 1000, 2000, 3000)
    print(d1.display_thank_you_letter())
    

def test_write_thank_you_letter():
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d1.write_thank_you_letter('.')
    assert os.path.isfile('./Maggie.txt')


def test_init_donor_collection():
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor('キラ', 9001)

    dc1 = dc(d1)
    dc1.add_donor(d2)
    dc1.add_donor(d3)

    print(dc1)

    assert d1 in dc1.collection
    assert d2 in dc1.collection
    assert d3 in dc1.collection


    assert False