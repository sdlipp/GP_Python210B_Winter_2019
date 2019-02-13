#!/usr/bin/env python3

import random
import re


word_reg = re.compile(r'\W+')  # regex to split text by white space


def populate_word_list(text_file):
    word_list = []
    with open(text_file, 'rt') as infile:
        lines = infile.readlines()
        for line in lines:
            for word in word_reg.split(line):
                if word:
                    word_list.append(word)
    return word_list


def build_pair_dictionary(word_list):
    pair_dict = {}
    for i in range(len(word_list) - 2):
        pair = ' '.join(word_list[i:i + 2])
        follower = word_list[i + 2]
        if pair not in pair_dict:  # Check if the pair is already in the dictionary
            pair_dict[pair] = [follower]
        else:
            pair_dict[pair].append(follower)
    return pair_dict


def build_new_text(pair_dict):
    trigram_list = []

    seed = random.choice(tuple(pair_dict.keys()))
    value = random.choice(pair_dict[seed])
    for word in seed.split():
        trigram_list.append(word)
    trigram_list.append(value)

    for i in range(10):
        if not pair_dict.get(trigram_list[-2] + trigram_list[-1]):
            seed = random.choice(tuple(pair_dict.keys()))
            value = random.choice(pair_dict[seed])

            for word in seed.split():
                trigram_list.append(word)
            trigram_list.append(value)

        else:
            trigram_list.append(random.choice(
                pair_dict.get(trigram_list[-2] + trigram_list)))

    full_text = f'{" ".join(trigram_list)}.'
    return full_text


if __name__ == '__main__':
    word_list = populate_word_list('sherlock.txt')
    pair_dict = build_pair_dictionary(word_list)
    full_text = build_new_text(pair_dict)
    print(full_text)


