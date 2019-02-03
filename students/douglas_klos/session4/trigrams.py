#!/usr/bin/env python3

# Douglas Klos
# January 31st, 2019
# Python 210, Assignment 4
# trigram.py

import string

def build_trigrams():
    trigrams = {}
    word_list = []

    start = 0

    intab = '-'
    outtab = ' '
    transtab = str.maketrans(intab, outtab)

    #startline = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    startline = 'Produced by an anonymous Project Gutenberg volunteer and Jose Menendez'
    #endline = '*** END OF THIS PROJECT GUTENBERG EBOOK'
    endline = 'End of the Project Gutenberg EBook'

    #[word for line in book for word in line.split()]
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

    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        follower = word_list[i+2]
        if pair not in trigrams:
            trigrams[pair] = [follower] 
        else:
            trigrams[pair] += [follower]

    for key in trigrams:
        print(f'{key} = {trigrams[key]}')
    #print(trigrams)    


def main():
    build_trigrams()


if __name__ == '__main__':
    main()
