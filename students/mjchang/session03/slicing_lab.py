#!/usr/bin/env python3

# exchange the first and last items
def exchange_first_last(seq):
    count = len(seq)
    return seq[-1:]+seq[1:count-1]+seq[:1]

str_test = "testing this string"
tuple_test = (23, 7, 41, 96, 5, 8)

assert exchange_first_last(str_test) == "gesting this strint"
assert exchange_first_last(tuple_test) == (8, 7, 41, 96, 5, 23)

# every other item is removed
def every_other(seq):
    seq = seq[::2]
    return seq

str_test = "testing this string"
tuple_test = (23, 7, 41, 96, 5, 8)

assert every_other(str_test) == "tsigti tig"
assert every_other(tuple_test) == (23, 41, 5)

#the first 4 and last 4 items and every other of the remaining are removed
def four_on_ends(seq):
    return seq[4:-4:2]

str_test = "testing this string"
tuple_test = (23, 7, 41, 96, 5, 8, 1000, 38, 17, 31, 14, 25, 2, 12, 4, 87, 15)

assert four_on_ends(str_test) == "igti t"
assert four_on_ends(tuple_test) == (5, 1000, 17, 14, 2)

