#!/usr/bin/env python3
'''
Here we go testing again!
'''
from donor_models import Donor
import cli_main


import pytest
import datetime
import os

'''
We'll start with testing the donor class
'''
def test_donor_init():
    donor = Donor("James Hetfield")
    assert donor.name == "James Hetfield"
    assert donor.donations == []
