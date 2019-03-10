#!/usr/bin/env python3

class SparseArray(object):

    def __init__(self, sequence=None):
        if sequence is None:
            self.sequence = []
        self.sequence = sequence
        self.display_list = [i for i in self.sequence if i >0]
        iterable = sequence
        self.create_working_dict(iterable)
        #self.create_working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}

    def create_working_dict(self):
        self.working_dict = {key: value for key, value in enumerate(self) if value > 0}

    #
    # def create_dictionary(self):
    #     self.working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}

    def __len__(self):
        return len(self.sequence)

    def append(self, val):
        if val == 0:
            return self.sequence
        self.sequence.append(val)

        self.working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}


    def __delitem__(self, key):
        del (self.working_dict[key])
        self.sequence.pop(key)

    def __getitem__(self, item):
        if item not in self.working_dict.keys():
            return 0
        else:
            return self.working_dict[item]

    def __setitem__(self, key, value):
        self.sequence[key] = value

    def __contains__(self, item):
        if self.sequence:
            return True

    def __repr__(self):
        return f'{self.sequence} has a length of {len(self.sequence)}'


if __name__ == '__main__':

    spa = SparseArray([1, 0, 2, 3])
    print(spa)
    print(len(spa))

    spa.append(10)
    print(spa)

    print(spa[2])
    del(spa[4])
    print(spa)

    # spa[5]=10
    # print(spa)
    # print(type(spa))
    # print(10 in spa)
