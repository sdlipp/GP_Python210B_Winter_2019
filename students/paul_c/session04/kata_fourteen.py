#!/usr/bin/env python3

import sys
import random

"""
This program was tested using the sherlock_small.txt and a_case_of_identity.txt files located in the working directory.

"""

def build_text(word_pairs):
        """
        Function to create a randomly generated list or words from a read in text file.
        :param word_pairs: Dictionary of word pairs created in build_trigrams function.
        :return: Randomized list of words that shuffles the contents of a text file to make a new "story".

        This function selects a random key, gets the value of that key, and appends the key and value to a new list.
        I feel like I missed something but I can't put my finger on it.
        """
        random_text = []
        while len(random_text) < len(word_pairs):
            random_key = random.choice(list(word_pairs.keys()))
            value = word_pairs.get(random_key)
            random_text.append(list(random_key))
            random_text.append(value)
            # I copied new_list line from the internet.
            # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
            new_list = [item for sublist in random_text for item in sublist]
            clean_text = " ".join(new_list)

        return clean_text


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):  # why -2 ?
        pair = words[i:i + 2]
        follower = words[i + 2]
        key_tuple = tuple(pair)
        trigrams.setdefault(key_tuple, []).append(follower)

    return trigrams


def make_words(string):
    """
    Function to create an ordered list of words from the text file input from read_in_data()
    :param string: Data read from text file in the read_in_data function.
    :return: Ordered list of words from read in text file.
    """
    split_string = string.split()

    return split_string


def read_in_data(text_file):
    """
    Function to open and read data from a text file.
    :param text_file: Text file passed in as an option when running the program.
    :return: Contents of the text file that was passed in.
    """
    open_file = open(text_file, "r")
    if open_file.mode == "r":
        read_file = open_file.read()

        return read_file


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)
