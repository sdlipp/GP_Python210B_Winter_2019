#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
#import random
#import os
#import re
#import itertools


def parse_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, strips punctuation and creates the main
    dictionary.
    Thanks for the help Luis!
    """
    temp_dict = {}
    sherlock_dict = {}
    translator = str.maketrans('', '', string.punctuation)
    sherlock_input = set(line.strip() for line in open('sherlock_small.txt'))

    for i in sherlock_input:
        i = i.translate(translator).split(' ')
        temp_dict = dict(i[l:l+2] for l in range(0, len(i) - 2))
        sherlock_dict = dict(list(sherlock_dict.items()) + \
        list(temp_dict.items()))
    create_tuples(sherlock_dict)


def create_tuples(sherlock_dict):
    """
    This should hopefully create the tuples needed for generating the trigrams
    """
    sherlock_tupled = []
    for i in sherlock_dict:
        k = (i, sherlock_dict[i])
        sherlock_tupled.append(k)
    print(list)


def main():
    """
    Main run list
    """
    parse_file()


if __name__ == "__main__":
    main()
