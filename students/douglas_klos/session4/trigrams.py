#!/usr/bin/env python3
""" This script generates new text from trigrams created from input file """

# Douglas Klos
# February 10th, 2019
# Python 210, Assignment 4
# trigram.py

import sys
import random
import time
import argparse

# I was able to increase this to about 16,800 on Ubuntu 18.04 before getting
# a segfault for stack overflow.  Milage may very.  Problem said to
# get around 100 words, so this seems like a viable solution.
# XPS 9570, i7-8750H, Ubuntu 18.04 - 16,500 words in .13 seconds.
# 2009 MacBook Pro, Core-2 Duo P8700, El Capitan - 16,500 in .44 seconds.

LENGTH = 500 # Now read in through command line
sys.setrecursionlimit(LENGTH + 3)

# Constants for random.normalvariate(MU, SIGMA)
MU = 125
SIGMA = 60

def is_project_gutenberg(filename):
    """ Determines if the book contains the Project Gutenberg string """
    startline = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    with open(filename) as book:
        for line in book:
            if line[:len(startline)] == startline:
                return True
    # Just a normal, non-gutenberg book
    return False


def read_normal_data(filename):
    """ Reads input file and generates a wordlist from it """

    word_list = []
    start = 0
    
    # Characters to filter out of the input text file.  Change to flavor.
    intab = '-'
    outtab = ' '
    transtab = str.maketrans(intab, outtab)

    with open(filename) as book:
        for line in book:
            newline = line.translate(transtab)

            for word in newline.split():
                word_list.append(word)

    return word_list


def read_gutenberg_data(filename):
    """ Reads input file and generates a wordlist from it """

    word_list = []
    start = 0
    
    # Characters to filter out of the input text file.  Change to flavor.
    intab = '-'
    outtab = ' '
    transtab = str.maketrans(intab, outtab)

    # String deliniating tne content of Project Gutenberg eBooks
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


def build_text(trigram_dictionary, LENGTH):
    """ Build new new_text from trigram_dictionary """

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
    """ Build new new_text from trigram_dictionary - recursive call """

    if length == 0:
        return new_text

    new_text.append(random.choice(trigram_dictionary[pair]))
    pair = (new_text[-2], new_text[-1])
    return build_text_recursive(trigram_dictionary, new_text, pair, length - 1)


def render_new_book(new_text):
    """ Returns a string containing the new text """
    new_text[0] = new_text[0].title()
    rendered_text = ''

    # Average paragraph length, according to a quick google search, is
    # 100 - 150 words.  We'll say the mean is 125 words per paragraph.
    # To have a variety of paragraph lengths, we do a normal distribution
    # with a mean of 125 and standard deviation (sigma) of 60.
    # Increase sigma for larger differences in length, decrease sigma
    # to cluster closer around the mean.
    paragraph_length = abs(random.normalvariate(MU, SIGMA))
    word_counter = 0

    for word in new_text:
        if word_counter >= paragraph_length:
            # This is the end of the paragraph.
            paragraph_length = abs(random.normalvariate(MU, SIGMA))
            word_counter = 0
            # The last character in the string is a space, we want it gone.
            rendered_text = rendered_text[:-1]
            # If we have a trailing comma, semi-colon, etc., erase it.
            if rendered_text[-1] in (',', ';', ':'):
                rendered_text = rendered_text[:-1]
            # If it ends in punctuation already, start new paragraph
            elif rendered_text[-1] in ('.', '?', '!'):
                rendered_text += ('\n\n')
                rendered_text += (word.title() + ' ')
            # Replace it with a '.' and begin a new paragraph.
            else:
                rendered_text += ('.\n\n')
                rendered_text += (word.title() + ' ')
        else:
            rendered_text += word + ' '
            word_counter += 1

    rendered_text = rendered_text[:-1]
    rendered_text += '.'

    return rendered_text


def main():
    """ trigrams.py main function """

    newbook = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        help="File to run trigrams on",
                        type=str)
    parser.add_argument("-o",
                        "--output",
                        help="Write new book to filename>.trigrams.txt",
                        action="store_true")
    args = parser.parse_args()
    start = time.time()

    if is_project_gutenberg(args.filename):
        word_list = read_gutenberg_data(args.filename)
    else:
        word_list = read_normal_data(args.filename)

    trigram_dictionary = build_dict(word_list)
    new_text = build_text(trigram_dictionary, LENGTH)
    newbook = (render_new_book(new_text))
    print(newbook)
    end = time.time()
    print()
    print(f'{len(new_text)} words genereated and formatted '
          f'in {abs(end-start)} seconds')

    if args.output:
        with open(str(args.filename[:-4]) + ".trigrams.txt", "w") as outfile:
            outfile.write(newbook)
            outfile.write(f'\n\n{str(LENGTH)} words rendered in '
                          f'{abs(end-start)} seconds')


if __name__ == '__main__':
    main()
