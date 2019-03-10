#!/usr/bin/env python3

import unittest

from sparse_array import *

class SparseArrayTest(unittest.TestCase):

    def test_init(self):
        spa = SparseArray([1, 2, 3])
        self.assertEqual(repr(spa), '[1, 2, 3] has a length of 3')
        del spa

    def test_get_length(self):
        spa = SparseArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(len(spa), 10)
        del spa

    def test_append(self):
        spa = SparseArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        spa.append(11)
        self.assertEqual(len(spa), 11)
        del spa

    def del_item_from_index(self):
        spa = SparseArray([1, 0, 2, 3])
        del(spa[1])
        self.assertEqual(spa.sequence, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
