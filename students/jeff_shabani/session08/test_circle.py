#!/usr/bin/env python3

import io
import pytest
import unittest

from Circle import *


c=Circle(5)

class mailroomTests(unittest.TestCase):


    def test_init(self):
        #c=Circle(5)
        self.assertEqual(c.radius, 5)

if __name__ == '__main__':
    unittest.main()