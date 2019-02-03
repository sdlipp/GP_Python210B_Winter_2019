#!/usr/bin/env python3
""" This script generates new text from trigrams created from input file """

# Douglas Klos
# February 3rd, 2019
# Python 210, Assignment 4
# trigram.py

import sys
import random
import time

# I was to increase this to about 16,800 on Ubuntu 18.04 before getting a
# seg fault for stack overflow.  Your milage may very.  Problem said to
# get around 100 words, so this seems like a viable solution.
# XPS 9570, i7-8750H, Ubuntu 18.04 - 16,500 words in .13 seconds.
# 2009 MacBook Pro, Core-2 Duo P8700, El Capitan - 16,500 in .44 seconds.
LENGTH = 500

# +3 because of the seeding for of initial list for recursion.
sys.setrecursionlimit(LENGTH+3)


def read_data(filename):
    """ Reads input file and generates a wordlist from it """

    word_list = []
    start = 0
    intab = '-'
    outtab = ' '
    transtab = str.maketrans(intab, outtab)

    startline = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    endline = '*** END OF THIS PROJECT GUTENBERG EBOOK'

    with open(filename) as book:
        for line in book:
            if line[:len(startline)] == startline:
                start = 1
                continue
            if not start:
                continue
            if line[:len(endline)] == endline:
                break
            newline = line.translate(transtab)

            for word in newline.split():
                word_list.append(word)

    return word_list


def build_dict(word_list):
    """ Given an input word list, generate trigrams """

    trigrams = {}

    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        follower = word_list[i+2]
        if pair not in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair] += [follower]

    return trigrams


def build_text(trigram_dictionary):
    """ Build new word_list from trigram_dictionary """

    new_text = []

    start_point = random.choice(tuple(trigram_dictionary.keys()))
    new_text.extend(start_point)
    new_text.extend(trigram_dictionary[start_point])

    start_case = (new_text[-2], new_text[-1])

    while True:
        try:
            return(build_text_recursive(trigram_dictionary,
                                        new_text, start_case, LENGTH-3))
        except KeyError:
            # We hit a dead-end, didn't find a recursive solution of
            # sufficient length.  Reset the initial conditions to
            # randoms and try again.
            start_point = random.choice(tuple(trigram_dictionary.keys()))
            new_text = []
            new_text.extend(start_point)
            new_text.extend(trigram_dictionary[start_point])
            start_case = (new_text[-2], new_text[-1])


def build_text_recursive(trigram_dictionary, new_text, pair, length):
    """ Build new word_list from trigram_dictionary """

    if length == 0:
        return new_text

    new_text.append(random.choice(trigram_dictionary[pair]))
    pair = (new_text[-2], new_text[-1])
    return build_text_recursive(trigram_dictionary, new_text, pair, length - 1)


def main():
    """ trigrams.py main function """

    start = time.time()
    try:
        filename = sys.argv[1]
    except IndexError:
        print('You must pass in a filename')
        sys.exit(1)

    word_list = read_data(filename)
    trigram_dictionary = build_dict(word_list)
    new_text = build_text(trigram_dictionary)

    new_text[0] = new_text[0].title()
    for word in new_text:
        print(f'{word} ', end='')

    end = time.time()
    print('\n')
    print(f'{len(new_text)} words genereated in {end-start} seconds')


if __name__ == '__main__':
    main()
