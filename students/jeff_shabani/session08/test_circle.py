#!/usr/bin/env python3
import unittest

from circle import *


class CircleTests(unittest.TestCase):

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
        self.assertEqual(c1 * 10, 20)
        self.assertEqual(c1 * 10 == 10 * c1, True)
        del c1, c2, c3

    def test_extended_assignment(self):
        c1 = Circle(12)
        c2 = Circle(10)
        c2 += c1
        c3 = c1.radius ** 2
        self.assertEqual(c2, 22)
        self.assertEqual(c3, 144)
        del c1, c2, c3

    # test for negative radius
    @unittest.expectedFailure
    def test_negative_radius(self):
        c1 = Circle(-1)
        self.assertEqual(c1, -1)
        del c1

    def test_sphere_volume(self):
        s = Sphere(1)
        self.assertEqual(s.volume(), 4.1887902047863905)
        del s

    def test_sphere_get_from_diameter(self):
        s = Sphere.from_diameter(4)
        self.assertEqual(s.volume(), 33.510321638291124)
        del s

    def test_sphere_printing(self):
        s = Sphere(10)
        self.assertEqual(repr(s),
                         'Sphere with radius of 10 volume of 4188.790204786391 & surface area of 1256.6370614359173')


if __name__ == '__main__':
    unittest.main()
