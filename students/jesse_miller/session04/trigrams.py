#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import random
import sys

def parse_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, strips punctuation and creates the main
    dictionary.
    Thanks for the help Luis!
    """
    startline = 'Produced by an anonymous Project Gutenberg'\
                'volunteer and Jose Menendez'
    endline = 'End of the Project Gutenberg EBook'

    with open('sherlock.txt') as input_file:
        input_file = [line.rstrip('\n') for line in input_file]
        full_list = []
        start = 0
        for line in input_file:
            if line[:len(startline)] == startline:
                start = 1
                continue
            if not start:
                input_file = [line.rstrip('\n') for line in input_file]
            if line[:len(endline)] == endline:
                break
    return full_list

def make_words(input_file):
    translator = str.maketrans('', '', string.punctuation)
    full_list = []
    for line in input_file:
        full_list.extend(line.translate(translator).split(' '))
    return full_list


def build_trigram(full_list):
    sherlock_dict = {}
    for i in range(0, len(full_list) - 2):
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        if trigram_key in sherlock_dict:
            sherlock_dict[trigram_key].append(trigram_value)
        else:
            sherlock_dict[trigram_key] = [trigram_value]
    return sherlock_dict

def build_text(sherlock_dict):
    pass

def main():
    """
    Main run list
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = parse_file()
    words = make_words(input_file)
    word_pairs = build_trigram(full_list)
    new_text = build_text(sherlock_dict)

    print(new_text)

if __name__ == "__main__":
    main()
