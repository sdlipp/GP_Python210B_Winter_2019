#!/usr/bin/env python3

class SparseArray(object):

    def __init__(self, sequence):
        self.sequence = sequence

    def __repr__(self):
        return f'{self.sequence}'

spa = SparseArray([1,2,3])

print(spa)
