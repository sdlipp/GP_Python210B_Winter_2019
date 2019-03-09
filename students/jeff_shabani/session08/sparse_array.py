#!/usr/bin/env python3

class SparseArray(object):

    def __init__(self, sequence, *seq_dict):
        self.sequence = sequence
        self.seq_dict = dict(seq_dict)

    def dict_convert(self):
        #seq_dict = dict()
        for k,v in enumerate(self.sequence):
            self.seq_dict[k]=v
        return self.seq_dict


    def __len__(self):
        return len(self.sequence)

    def __setitem__(self, key, value):
        self.sequence[key] = value


    def __repr__(self):
        return f'{self.seq_dict.values()} has a length of {len(self.sequence)}'

spa = SparseArray([1,2,3])

print(len(spa))

spa[1] = 2
print(spa)
