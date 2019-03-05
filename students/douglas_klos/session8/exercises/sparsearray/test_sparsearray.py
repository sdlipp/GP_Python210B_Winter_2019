#!/usr/bin/env python3

""" Pytest file for sparsearray.py """

# Douglas Klos
# March 5th, 2019
# Python 210, Session 8
# test_sparsearray.py


import pytest
from sparsearray import SparseArray


def test_sparsearray_init():
    """ Tests that a sparsearray can be initialized """
    sa = SparseArray([1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
    print(sa.array)
    assert sa.array[0] == sa.array[4] == sa.array[5] == sa.array[10] == sa.array[14] == 1


def test_sparsearray_len():
    list1 = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    sa = SparseArray([1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
    print(sa)
    assert len(sa) == len(list1)
    assert False


def test_sparsearray_set_value():
    list1 = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    sa = SparseArray(list1)

    print(sa)
    sa[1] = 2
    sa[2] = 0
    print(sa)
    assert False