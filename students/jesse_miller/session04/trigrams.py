#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import random
#import os
import re
import itertools


def parse_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, strips punctuation and creates the main
    dictionary.
    Thanks for the help Luis!
    """
    translator = str.maketrans('', '', string.punctuation)
    with open('sherlock_small.txt') as input_file:
        full_list = []
        for line in input_file:
            full_list.extend(line.translate(translator).split(' '))
    # At this point, we have a big list with all the words in the text, no trigrams yet

    sherlock_dict = {}
    for i in range(0, len(full_list) - 2):
        # This will make the trigram key a two-element tuple
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        # Check if this key is already in the dictionary
        if trigram_key in sherlock_dict:
            # Append it to the list of values associated to the key
            sherlock_dict[trigram_key].append(trigram_value)
        else:
            # Initialize the new key
            sherlock_dict[trigram_key] = [trigram_value]
    create_trigram(sherlock_dict)


def create_trigram(sherlock_dict):
    """
    This should hopefully create the tuples needed for generating the trigrams
    """
    token = ""
    sherlock_tupled = {}
    sherlock_value = ','.join(str(sherlock_dict) for v in sherlock_dict)
    sherlock_value = sherlock_value.lower()
    s = ""
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    #print(sherlock_value)
    sherlock_list = [token for token in s.split(" ") if token != ""]
    trigrams = zip(*[sherlock_list[i:] for i in range(3)])
    return [" ".join(sherlock_list) for i in sherlock_list]


def main():
    """
    Main run list
    """
    parse_file()


if __name__ == "__main__":
    main()
