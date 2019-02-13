#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

def exchange_first_last(seq):
    """
    Function that returns a sequence with the fist and last items exchanged.
    """
    length = len(seq) -1
    new_seq = seq[-1:]+seq[1:length]+seq[:1]
    return new_seq

def remove_every_other(seq):
    """ Function that returns a sequence with every other item removed."""
    length = len(seq)
    new_seq = seq[0:length:2]
    return new_seq

def fours_removed(seq):
    """
    Functon that removes from a sequence the first 4 items and last 4 items,
    and then returns every other item remaining in the sequence.
    """
    length = len(seq) - 4
    new_seq = seq[4:length:2]
    return new_seq

def elements_reversed(seq):
    """ Function that returns a sequence with its elements reversed."""
    new_seq = seq[::-1]
    return new_seq

def rearrange_thirds(seq):
    """
    Function that returns the items representing the last third of a sequence,
    followed by the items representing the first third of the sequence,
    followed by the items representing the middle third of the sequence.
    """
    length = int(len(seq) / 3)
    new_seq = seq[-length:] + seq[:length] + seq[length:-length]
    return new_seq


if __name__ == '__main__':
    # Run Some Tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (2, 67, 14, 17, 24, 63, 14, 9, 98, 39, 28, 12)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert fours_removed(a_long_tuple) == (24, 14)
    assert fours_removed(a_string) == " sas"

    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert elements_reversed(a_string) == "gnirts a si siht"

    assert rearrange_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert rearrange_thirds(a_string) == "tringthis is a s"

    print("Tests Passed")
