#!/usr/bin/env python3

import unittest

from sparse_array import *

class SparseArrayTest(unittest.TestCase):

    def test_init(self):
        spa = SparseArray([1, 2, 3])
        self.assertEqual(repr(spa), '{0: 1, 1: 2, 2: 3} has a length of 3')
        self.assertIsInstance(spa, SparseArray)
        del spa

    def test_length(self):
        spa = SparseArray([1,2,3,4])
        self.assertEqual(len(spa), 4)
        del spa

    def test_append(self):
        spa = SparseArray([1, 2, 3, 4])
        spa[4]=10
        self.assertIn(10, spa)



if __name__ == '__main__':
    unittest.main()
