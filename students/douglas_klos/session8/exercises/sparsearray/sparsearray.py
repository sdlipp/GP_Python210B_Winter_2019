#!/usr/bin/env python3

""" SparseArray Class """

# Douglas Klos
# March 5th, 2019
# Python 210, Session 8
# sparsearray.py


class SparseArray():
    """ SparseArray class """

    def __init__(self, values):
        self.array = {}
        self.length = len(values)

        for i in range(len(values)):
            if values[i] != 0:
                self.array[i] = values[i]

    def __str__(self):
        values = [value for key, value in sorted(self.array.items())]
        return str(values)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        if value:
            self.array[key] = value
