#!/usr/bin/env python3

# Lesson 04 Exercise: Trigrams
# Jeremy Monroe

import random
import os

words = "I wish I may I wish I might".split()


def build_trigrams_dict(words):
    """ This function takes in a list of strings.

        And processes those strings to populate a dictionary where the structure is 
        a key of two consecutive strings in the list and the value is a list of 
        all possible strings that come after the key in the original list.
    """
    trigrams_dict = {}

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]

        string_pair = ' '.join(pair)

        if string_pair in trigrams_dict:
            trigrams_dict[string_pair].append(follower)
        else:
            trigrams_dict[string_pair] = [follower]

    return trigrams_dict


def build_trigrams(trigrams_dict):
    """ This function takes the dict that has been built by build_trigrams_dict
         and uses it to form a new string following a trigram pattern. 

         Using a random key to start it populates a list with the key and one
         of its values and repeats the process using the last two strings in
         the list as the new key.

         If the new key isn't in the trigram dict it will start again with a
         randomly chosen key.
    """
    trigrams_list = []

    first_key = random.choice(list(trigrams_dict.keys()))
    first_value = random.choice(trigrams_dict[first_key])
    for stringy in first_key.split():
        trigrams_list.append(stringy)
    trigrams_list.append(first_value)

    for i in range(100):
        if not trigrams_dict.get(trigrams_list[-2] + trigrams_list[-1]):
            first_key = random.choice(list(trigrams_dict.keys()))
            first_value = random.choice(trigrams_dict[first_key])

            for stringy in first_key.split():
                trigrams_list.append(stringy)
            trigrams_list.append(first_value)

        else:
            trigrams_list.append(random.choice(
                trigrams_dict.get(trigrams_list[-2] + trigrams_list)))

    return ' '.join(trigrams_list)


def read_in_data(filename):
    """ This function takes in a filename, opens that file, modifies the start 
        and end of the file, filters out specific characters, and returns it as 
        a list.
    """
    # ↓ These ↓ characters will be replaced by spaces in the string
    bad_chars = ',()[]-";'

    with open(filename, 'r') as sherly:
        str_sherly = sherly.read()

        str_sherly = str_sherly.split('*** START OF THIS PROJECT', 1)[-1]
        str_sherly = str_sherly.split('End of the Project Gutenberg', 1)[0]

        for bad_char in bad_chars:
            str_sherly = str_sherly.replace(bad_char, ' ')

    return str_sherly.split()


def clear_screen():
    """ Clears the terminal screen """
    os.system('cls') if os.name == 'nt' else os.system('clear')


if __name__ == '__main__':
    clear_screen()
    print('Either ensure your file is in the current working directory')
    print('Or provide an absolute path')
    filename = input('Please input a filename:\n--->')
    clear_screen()

    in_data = read_in_data(filename)
    trigrams_dict = build_trigrams_dict(in_data)
    trigrams = build_trigrams(trigrams_dict)

    print(trigrams)
