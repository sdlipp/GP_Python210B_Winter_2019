#!/usr/bin/env python3
import unittest

from donor import *

class OOMailroonTests(unittest.TestCase):

    def test_add_donor(self):
        d = Donor()
        d.add_donor('Katherine', [100, 500, 610])
        print(d.donors)