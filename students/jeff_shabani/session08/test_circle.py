#!/usr/bin/env python3

import unittest

from Circle import *


class circleTests(unittest.TestCase):

    def test_init(self):
        """test for instantiation"""
        c = Circle(5)
        self.assertEqual(c.radius, 5)
        del c

    def test_diameter_calc(self):
        c = Circle(4)
        self.assertEqual(c.diameter, c.radius * 2)
        del c

    def test_diameter_setter(self):
        c = Circle(5)
        self.assertEqual(c.diameter, 10)
        c.diameter = 24
        self.assertEqual(c.diameter, 24)
        self.assertEqual(c.radius, 12)
        del c

    def test_area(self):
        c = Circle(5)
        self.assertEqual(c.area, math.pi * pow(c.radius, 2))
        del c

    def test_from_diameter(self):
        c = Circle.from_diameter(6)
        self.assertEqual(c.radius, 3)
        self.assertEqual(c.diameter, 6)
        del c

    def test_print(self):
        c = Circle(8)
        self.assertEqual(repr(c), 'Circle with radius of 8')
        del c

    def test_math(self):
        c1 = Circle(2)
        c2 = Circle(3)
        self.assertEqual(c1 + c2, 5.0)
        self.assertEqual(c1 * 5, 10.0)
        # this tests argument reversal in mult function
        self.assertEqual(5 * c1, 10.0)
        del c1, c2

    def test_compare_circles(self):
        c1 = Circle(2)
        c2 = Circle(3)
        c3 = Circle(3)
        self.assertEqual(c1 > c2, False)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 != c2, True)
        self.assertEqual(c3 == c2, True)
        self.assertEqual(c1 * c2, 6.0)


if __name__ == '__main__':
    unittest.main()
