#!/usr/bin/env python3

import io
import pytest
import unittest

from Circle import *


c=Circle(5)

class mailroomTests(unittest.TestCase):


    def test_init(self):
        """test for instantiation"""
        self.assertEqual(c.radius, 5)

    def test_diameter_calc(self):
        self.assertEqual(c.diameter, c.radius*2)

    def test_diameter_setter(self):
        c.diameter = 24
        self.assertEqual(c.diameter, 24)

if __name__ == '__main__':
    unittest.main()