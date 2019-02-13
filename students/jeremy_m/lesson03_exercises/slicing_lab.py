#!/usr/bin/env python3
# Lesson 03 - Slicing Lab
# Jeremy Monroe

def first_to_last(seq):
    """ Swaps the first and last items in a sequence. """
    return seq[-1] + seq[1:-1] + seq[0]

# print(first_to_last('hello'))
assert first_to_last('dingle') == 'eingld'
assert first_to_last('hello') == 'oellh'


def every_other(seq):
    """ Returns a sequence with every other item removed """
    return seq[::2]

# print(every_other('hello'))
assert every_other('hello') == 'hlo'
assert every_other('cornholio') == 'crhlo'


def first_four_last_four(seq):
    """ Removes the first four and last four items and then removes every other
        item from what is left. """
    return seq[4:-4:2]

# print(first_four_last_four("I'll need a long sequence for this"))
assert first_four_last_four("I'll need a long sequence for this") == ' edaln eunefr'
assert first_four_last_four('Many mangy monkeys') == ' ag o'


def reverso(seq):
    """ Returns a sequence in reverse order. """
    return seq[::-1]

# print(reverso('ham sammich'))
assert reverso('ham sammich') == 'hcimmas mah'
assert reverso('Turkey sandwhich') == 'hcihwdnas yekruT'


def thirds_reversal(seq):
    """ Returns a sequence with what was the last third now first, followed by
        the first third, and middle third. """
    return seq[-(len(seq) // 3):] + seq[:-(len(seq) // 3)]

# print(thirds_reversal('easy string'))
assert thirds_reversal('easy string') == 'ingeasy str'
assert thirds_reversal('twelve letters ') == "ters twelve let"