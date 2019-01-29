#!/usr/bin/env python3

# Douglas Klos
# Python 210, Exerise 3
# January 24th 2019
# slice_lab.py


def exchange_first_last(seq):
    """ Exchanges the first and lest items in the sequence """
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """ Removes every other item in the sequence """
    return seq[::2]


def first4_last4_every_other(seq):
    """ Removes the first four, last four, and every other item """
    return seq[4:-4:2]


def reverse(seq):
    """ Returns the sequence in reverse order """
    return seq[::-1]


def thirds(seq):
    """
    Returns the last third, the first third, then the middle third.
    'one_third' is estimated to be the floor of the length divided by 3.
    Some 'thirds' are larger than others, unless the length % 3 == 0
    """
    one_third = len(seq) // 3
    return seq[2*one_third:] + seq[:one_third] + seq[one_third:2*one_third]


def main():
    """ slice.py main """
    a_string = 'this is a string'
    b_tuple = (2, 54, 13, 12, 5, 32)
    c_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(b_tuple) == (2, 13, 5)
    assert remove_every_other(c_tuple) == (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(b_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(c_tuple) == (20, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                            12, 13, 14, 15, 16, 17, 18, 19, 1)

    assert first4_last4_every_other(a_string) == ' sas'
    assert first4_last4_every_other(b_tuple) == ()
    assert first4_last4_every_other(c_tuple) == (5, 7, 9, 11, 13, 15)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(b_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse(c_tuple) == (20, 19, 18, 17, 16, 15, 14, 13, 12,
                                11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert thirds(a_string) == 'stringthis is a '
    assert thirds(b_tuple) == (5, 32, 2, 54, 13, 12)
    assert thirds(c_tuple) == (13, 14, 15, 16, 17, 18, 19, 20, 1,
                               2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    print('tests passed')


if __name__ == '__main__':
    main()
