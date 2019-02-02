#!/usr/local/bin/python3

def exchange_first_last(sequence):
    """
    Function to swap the first and last values in a given sequence.
    :param sequence: A sequence. In this case a tuple, string, and list.
    :return: The sequence with its first and last values swapped.
    """
    first = sequence[:1]
    last = sequence[-1:]
    middle = sequence[1:-1]
    new_sequence = last + middle + first
    return new_sequence


def remove_every_other(sequence):
    """
    Function to remove every other value in a given sequence.
    :param sequence: A sequence. In this case a tuple, string, and list.
    :return: The sequence with every even value removed.
    """
    new_sequence = sequence[::2]
    return new_sequence


def first_last_four(sequence):
    """
    Function to remove every value that is not contained in the first 4 or last 4 values.
    :param sequence: A tuple with 10 values.
    :return: A concatonation of the first 4 and last 4 values of the sequence.

    This function should return (1, 2, 3, 4, 7, 8, 9, 10). (5, 6) should be left out.
    """
    first_four = sequence[:4]
    last_four = sequence[-4:]
    new_sequence = first_four + last_four
    return new_sequence


def elements_reversed(sequence):
    """
    Function to reverse the values in a given sequence using only slice.
    :param sequence: A sequence. In this case a tuple, string, and list.
    :return: The sequence in reverse.
    """
    reverse_sequence = sequence[::-1]
    return reverse_sequence


def in_thirds(sequence):
    """
    Function to return a sequence divided by thirds and returned out of order.
    :param sequence: A tuple with 10 values.
    :return: The sequence with values in the following order. Last third, first third, middle third.

    I was not sure how to do this. A third represents .33% of a sequence.
    However, slices are not compatible with floats.
    """
    size = len(sequence)
    third = int(size * 0.33)
    first_third = sequence[0:third]
    length = len(first_third)
    middle_third = sequence[length:-length]
    two_lengths = length * 2
    last_third = sequence[two_lengths:-1]
    return last_third + first_third + middle_third


a_string = "Test string!!!"
a_tuple = (1, 2, 3, 4, 5)
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a_list = ['one', 'two', 'three', 'four', 'five']

# Tests for first function.
assert exchange_first_last(a_string) == '!est string!!T'
assert exchange_first_last(a_tuple) == (5, 2, 3, 4, 1)
assert exchange_first_last(a_list) == ['five', 'two', 'three', 'four', 'one']
# Tests for second function.
assert remove_every_other(a_string) == 'Ts tig!'
assert remove_every_other(a_tuple) == (1, 3, 5)
assert remove_every_other(a_list) == ['one', 'three', 'five']
# Tests for third function.
assert first_last_four(b_tuple) == (1, 2, 3, 4, 7, 8, 9, 10)
# Tests for fourth function.
assert elements_reversed(a_string) == "!!!gnirts tseT"
assert elements_reversed(a_tuple) == (5, 4, 3, 2, 1)
# Tests for fifth function.
in_thirds(b_tuple)






