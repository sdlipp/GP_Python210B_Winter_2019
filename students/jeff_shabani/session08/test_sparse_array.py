#!/usr/bin/env python3

import unittest

from sparse_array import *

class SparseArrayTest(unittest.TestCase):

    def test_init(self):
        spa = SparseArray([1, 2, 3])
        self.assertEqual(repr(spa), '[1, 2, 3]')


if __name__ == '__main__':
    unittest.main()
