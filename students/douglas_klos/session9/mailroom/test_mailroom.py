#!/usr/bin/env python3
""" Mailroom OO pytest """

# Douglas Klos
# March 12th, 2019
# Python 210, Session 9, Mailroom OO
# test_mailroom.py


from donor import Donor


def test_init():
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    
    assert d1.name == 'Maggie'
    assert d2.name == 'Doug'
    assert 1000 in d2.donations


def test_add_donation():
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)

    d1.add_donation(1000)
    d2.add_donation(2000)
    d2.add_donation(3000)

    assert 1000 in d1.donations
    assert 1000 in d2.donations
    assert 2000 in d2.donations
    assert 3000 in d2.donations
    assert 2000 not in d1.donations


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
    # d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)

    assert d1.total_donations == 6000
    d1.add_donation(4000)
    assert d1.total_donations == 10000
    d1.remove_donation(1000)
    assert d1.total_donations == 9000



# def test_donations_property():
#     d1 = Donor('Maggie')
#     d2 = Donor('Doug', 1000)
    
#     d1.donations = 1000
#     d2.donations = 2000
#     d2.donations = 3000
#     del(d2.donations[2000])
    
#     print(d1.donations)
#     print(d2.donations)

#     assert False