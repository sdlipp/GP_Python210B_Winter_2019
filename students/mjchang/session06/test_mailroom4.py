#!/usr/bon/env python3


import os
import sys
import unittest

import mailroom4

mr4.donor_db = mailroom4.donor_db()

def test_donor_list():
    """ test to see if donors are showing up in list"""
    donors = mr4.donor_db.keys()
    assert len(donors.split('\n')) == 5
    assert "Tao Chien" in donors
    assert "Eliza Sommers" in donors


def test_no_donor_search():
    """ test that a new donor doesn't show up"""
    donor = mr4.donor_db.keys()
    assert donor is None



def test_donor_search():
    """ test that an existing donor is there
also test if existing donor can be found using different capitalization inputs"""
    donor = mr4.donor_db.keys()
    assert donor[2] == "Joaquin Andieta"
    assert donor[4] == "Jacob Todd"



def test_gen_single_letter():
    """test that the donor letter/message is generated"""
    pass


def test_donor_addition():
    """ test that new donor is added"""
    pass


def test_create_report():
    """ test that the donor report is created and displayed correctly"""
    pass


def test_gen_letters():
    """ test that letters were generated and saved to the specified folder"""
    pass


if __name__ == "__main__":
    test_donor_list()
    test_no_donor_search()
    test_donor_search()
    test_gen_single_letter()
    test_donor_addition()
    test_create_report()
    test_gen_letters()
    print("All the tests passed!")

