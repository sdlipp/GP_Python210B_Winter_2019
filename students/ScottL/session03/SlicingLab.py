sequence1 = "This is a random string"
sequence2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def exchange_first_last(sequence):
    """Return a sequence with the first and last elements exchanged for one another."""
    return sequence[-1:] + sequence[1:-1] + sequence[:1]


assert exchange_first_last(sequence1) == "ghis is a random strinT"
assert exchange_first_last(sequence2) == (10, 2, 3, 4, 5, 6, 7, 8, 9, 1)


def remove_every_other(sequence):
    """Return a sequence with every other item removed"""
    return sequence[::2]

assert remove_every_other(sequence1) == "Ti sarno tig"
assert remove_every_other(sequence2) == (1, 3, 5, 7, 9)


def first4removed_last4removed_every_other(sequence):
    """Return a sequence where the first 4 and last 4 elements are removed and then every other element is displayed"""
    return sequence[4:-4:2]

assert first4removed_last4removed_every_other(sequence1) == " sarno t"
assert first4removed_last4removed_every_other(sequence2) == (5,)


def reverse_order(sequence):
    """Return a sequence with the order reversed"""
    return sequence[::-1]

assert reverse_order(sequence1) == "gnirts modnar a si sihT"
assert reverse_order(sequence2) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


def last3rd_first3rd_middle3rd(sequence):
    """Return a sequence with the last third of the sequence first, then the first third and finally the middle third"""
    i = round((len(sequence)) / 3)
    j = round(2 * len(sequence) / 3)
    return sequence[j:] + sequence[:i] + sequence[i:j]

assert last3rd_first3rd_middle3rd(sequence1) == "m stringThis is a rando"
assert last3rd_first3rd_middle3rd(sequence2) == (8, 9, 10, 1, 2, 3, 4, 5, 6, 7)