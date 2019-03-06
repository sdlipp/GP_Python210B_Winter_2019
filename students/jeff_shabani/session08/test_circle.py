#!/usr/bin/env python3

import io
import pytest
import unittest

from Circle import *


def test_init():
    c = Circle(5)

    assert print(c) == 6, 'Not equal'

# c = Circle(8)
# print(c.radius)
# class mailroomTests(unittest.TestCase):
#
#     def test_init(self):
#         c=Circle(5)
#         self.assertEqual(print(c.radius), 5)
#
# if __name__ == '__main__':
#     unittest.main()