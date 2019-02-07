#!/usr/bin/env python3

import random
import re

word_reg = re.compile(r'\W+')  # regex to split text by white space


# read in the text file and parse the words
def trigram(file):
    pair_dict = dict()
    word_list = []

    with open(file, 'rt') as infile:
        lines = infile.readlines()
        for line in lines:
            for word in word_reg.split(line):
                if word:
                    word_list.append(word)

    # build the dictionary
    for i in range(len(word_list) - 2):
        pair = ' '.join(word_list[i:i + 2])
        follower = word_list[i + 2]
        if pair not in pair_dict:  # Check if the pair is already in the dictionary
            pair_dict[pair] = [follower]
        else:
            pair_dict[pair].append(follower)


    # build the trigram list
    trigram_list = list()

    key, value = next(iter(pair_dict.keys())), next(
        iter(pair_dict.values()))  # split a single key, value pair into two variables.

    key1, key2 = key.split()  # split key into two words

    trigram_list.append(key1)
    trigram_list.append(key2)

    trigram_list.append(value[0])  # value is returned as a list, so extract the first list item

    # build the trigram string
    for i in range(1, 50):
        seed = " ".join(trigram_list[i:i + 2])  # get right-most two words in current list

        trigram_list.append(pair_dict.get(seed)[0])  # with seed as key append the corresponding value to trigram list

    print(f'{" ".join(trigram_list)}.')


trigram('sherlock.txt')
