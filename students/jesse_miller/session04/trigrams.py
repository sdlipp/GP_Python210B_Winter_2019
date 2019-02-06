#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
#import random
#import os
#import re
#import itertools


def open_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, as well as strips punctuation.  Thanks
    for the help Luis!
    """
    sherlock_dict = {}
    translator = str.maketrans('', '', string.punctuation)
    sherlock_input = set(line.strip() for line in open('sherlock_small.txt'))
    for i in sherlock_input:
        i = i.translate(translator).split(' ')
        print(i)
#    for w in range(len(i)):
#        sherlock_dict.append({get_var_name(key): key[l] for key in keys})
#    print("")
#    print(sherlock_dict)


# for item in i:
#    sherlock_dict = dict(itertools.zip_longest(*[iter(i)] * 2, fillvalue=""))
# print(sherlock_dict)
# munge_file(sherlock_input)


def main():
    """
    Main run list
    """
    open_file()


if __name__ == "__main__":
    main()
