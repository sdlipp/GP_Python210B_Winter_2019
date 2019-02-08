#!/usr/bin/env python3

# Lesson 04 Exercise: Trigrams
# Jeremy Monroe

import random
import os

words = "I wish I may I wish I might".split()


def build_trigrams(words):
    trigrams = {}
    trigrams_list = []

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]

        string_pair = ' '.join(pair)

        if string_pair in trigrams:
            trigrams[string_pair].append(follower)
        else:
            trigrams[string_pair] = [follower]

    first_key = random.choice(list(trigrams.keys()))
    first_value = random.choice(trigrams[first_key])
    for stringy in first_key.split(): trigrams_list.append(stringy)
    trigrams_list.append(first_value)

    # while trigrams.get(trigrams_list[-2] + trigrams_list[-1]):
    for i in range(100):
        if not trigrams.get(trigrams_list[-2] + trigrams_list[-1]):
            for stringy in first_key.split(): trigrams_list.append(stringy)
            trigrams_list.append(first_value)
            first_key = random.choice(list(trigrams.keys()))
            first_value = random.choice(trigrams[first_key])
        else:
            trigrams_list.append(random.choice(trigrams.get(trigrams_list[-2] + trigrams_list)))
    
    return ' '.join(trigrams_list)


if __name__ == '__main__':
    bad_chars = ',()[]-"'
    with open('sherlock.txt', 'r') as sherly:
        str_sherly = sherly.read()

        str_sherly = str_sherly.split('ADVENTURE I. A SCANDAL IN BOHEMIA\n\nI.\n', 1)[-1]

        for bad_char in bad_chars:
            str_sherly = str_sherly.replace(bad_char, ' ')
        trigrams = build_trigrams(str_sherly.split())
    print(trigrams)
