#!/usr/bin/env python3
'''
Here we go testing again!
'''
import datetime
import os
import pytest

from donor_models import Donor
import cli_main
'''
We'll start with testing the donor class
'''
def test_donor_init():
    '''
    This tests adding a donor
    '''
    donor = Donor('James Hetfield')
    assert donor.name == 'James Hetfield'
    assert donor.donations == []


def test_donor_init_error():
    '''
    Now, let's see if we can break it
    '''
    with pytest.raises(TypeError):
        #pylint: disable=E1121
        Donor('Kirk Hammett', 400)


def test_donation_add():
    '''
    Let's try to add money the right way
    '''
    donor = Donor('James Hetfield')
    donor.donation_add(400)

    assert donor.donations == [400]

    donor.donation_add(3000)
    assert donor.donations == [400, 3000]
