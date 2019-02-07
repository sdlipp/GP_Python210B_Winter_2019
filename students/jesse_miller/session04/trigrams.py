#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import random
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
        sherlock_dict = dict(list(sherlock_dict.items()) +
                             list(temp_dict.items()))
    create_tuples(sherlock_dict)


def create_tuples(sherlock_dict):
    """
    This should hopefully create the tuples needed for generating the trigrams
    """
    sherlock_tupled = {}

    for i in range(len(sherlock_dict) - 2):
        pair = ' '.join(sherlock_dict[i:i + 2])
        follower = sherlock_dict[i + 2]
        if pair not in sherlock_tupled:  # Check if the pair is already in the dictionary
            sherlock_tupled[pair] = [follower]
        else:
            sherlock_tupled[pair].append(follower)



def trigram_gen(sherlock_tupled):
    """
    This, should assemble the randomized texts
    """
    print("I am Sherlock tupled:")
    print(sherlock_tupled)
    print("I am Sherlock reconstructed:")
    for i in sherlock_tupled:
        text = random.sample(sherlock_tupled, 8)


def main():
    """
    Main run list
    """
    parse_file()


if __name__ == "__main__":
    main()
