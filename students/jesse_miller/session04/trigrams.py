#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import random
import csv
import re

def parse_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, strips punctuation and creates the main
    dictionary.
    Thanks for the help Luis!
    """
    translator = str.maketrans('', '', string.punctuation)
    with open('sherlock_small.txt') as input_file:
        input_file = [line.rstrip('\n') for line in input_file]
        full_list = []
        for line in input_file:
            full_list.extend(line.translate(translator).split(' '))

    sherlock_dict = {}
    for i in range(0, len(full_list) - 2):
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        if trigram_key in sherlock_dict:
            sherlock_dict[trigram_key].append(trigram_value)
        else:
            sherlock_dict[trigram_key] = [trigram_value]

    for key in sherlock_dict:
        print(f'{key}) = {sherlock_dict[key]}')

    return sherlock_dict

    pass

def main():
    """
    Main run list
    """
    parse_file()


if __name__ == "__main__":
    main()
