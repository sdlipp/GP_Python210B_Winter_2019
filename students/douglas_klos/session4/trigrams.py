#!/usr/bin/env python3

# Douglas Klos
# February 2nd, 2019
# Python 210, Assignment 4
# trigram.py


import sys


def read_data(filename):
    """ Reads input file and generates a wordlist from it """

    word_list = []
    start = 0
    intab = '-'
    outtab = ' '
    transtab = str.maketrans(intab, outtab)

    # startline = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    startline = 'Produced by an anonymous Project Gutenberg'\
                'volunteer and Jose Menendez'
    # endline = '*** END OF THIS PROJECT GUTENBERG EBOOK'
    endline = 'End of the Project Gutenberg EBook'

    with open('sherlock.txt') as book:
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

    for key in trigrams:
        print(f'{key} = {trigrams[key]}')

    return trigrams
    # print(trigrams)


def build_text(trigram_dictionary):
    pass


def main():

    # get file from command prompt
    try:
        filename = sys.argv[1]
    except IndexError:
        print('You must pass in a filename')
        sys.exit(1)

    word_list = read_data(filename)
    trigram_dictionary = build_dict(word_list)
    new_text = build_text(trigram_dictionary)


if __name__ == '__main__':
    main()
