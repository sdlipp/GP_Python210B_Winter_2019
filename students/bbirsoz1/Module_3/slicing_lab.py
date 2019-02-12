#SLICING LAB
"""
def exchange_first_last(seq):
    return a_new_sequence
"""

#1)With the first and last items exchanged.
def exchange_first_last(seq):
    last = seq[-1:]
    middle = seq[1:-1]
    first = seq[0:1]
    return last + middle + first

#2)With every other item removed.
def every_other_removed(seq):
    return seq[::2]

#3)With the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def first_last_4_every_other_removed(seq):
    seq_a = seq[4:-4]
    return seq_a[::2]

#4)With the elements reversed (just with slicing).
def elements_reversed(seq):
    return seq[::-1]

#5)With the last third, then first third, then the middle third in the new order.
def last_first_middle(seq):
    last3_seq = seq[-3:]
    first3_seq = seq[:3]
    middle = len(seq)//2
    middle3_seq = seq[middle-1:middle+2]
    return last3_seq + first3_seq + middle3_seq

#TESTS
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a2_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other_removed(a_string) == "ti sasrn"
assert every_other_removed(a_tuple) == (2, 13, 5)

assert first_last_4_every_other_removed(a_string) == " sas"
assert first_last_4_every_other_removed(a2_tuple) == (4, 6, 8, 10, 12, 14)

assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert last_first_middle(a_string) == "ingthi a "
assert last_first_middle(a_tuple) == (12, 5, 32, 2, 54, 13, 13, 12, 5)

print("test completed")
