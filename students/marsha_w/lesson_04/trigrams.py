#!/usr/bin/env python3

'''
Title:Dictionary Lab Exercise
Dev: Marsha Wheeler
Date:02/09/2019
'''

import sys
import random

def clean_text(file):
    good_words = []
    with open(file) as f:
        header = False
        for lines in f:
            if lines.startswith('***') or lines.startswith('\n'):
                header = True
                continue
            else:
                words = lines.rstrip('\n').split()
                for word in words:
                    if word.isupper() and len(word) > 1:
                        continue
                    elif word.startswith('www') or word.startswith('http'):
                        continue
                    elif '[' in word or ']' in word :
                        continue
                    else:
                        good_words.append(word.strip('()').strip('""'))
    return(good_words)

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    # build up the dict here
    for i in range(len(words)-2):
        pair = words[i] + " " + words[i + 1]
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


def build_text(dict):
    """
    uses random to generate new text
    """
    # generate new text here
    new_text = []
    count = 0
    while count < 10:
        count = count + 1
        random_key = random.choice(list(dict.keys()))
        random_value = random.choice(dict.get(random_key))
        random_text = random_key + " " + random_value
        new_text.append(random_text)
        final_text = " ".join(new_text)

    return final_text




if __name__ == "__main__":
    try:
        myFile = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    sample_text = clean_text(myFile)
    #print(sample_text)
    trigrams = build_trigrams(sample_text)
    new_text = build_text(trigrams)
    print(new_text)
