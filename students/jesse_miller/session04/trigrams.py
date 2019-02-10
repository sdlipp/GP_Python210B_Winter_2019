#!/usr/local/bin/python3
"""
Trigrams attempt number 223123041.  I feel awful that I needed this much help
with this assignment.  Hopefully I'll do better in the future.
"""
import string
import random
import sys


def parse_file(filename):
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list, strips \n  and creates the main
    word list.
    Thanks for the help Luis!
    """
    startline = 'Produced by an anonymous Project Gutenberg'\
                'volunteer and Jose Menendez'
    endline = 'End of the Project Gutenberg EBook'
    start = 0

    with open(filename) as input_file:
        #input_file = [line.rstrip('\n') for line in input_file]
        for line in input_file:
            if line[:len(startline)] == startline:
                start = 1
                continue
            if not start:
                input_file = [line.rstrip('\n') for line in input_file]
            if line[:len(endline)] == endline:
                break
    return input_file


def make_words(input_file):
    """
    This function finishes out the the word list, removes punctuation.
    """
    translator = str.maketrans('', '', string.punctuation)
    full_list = []
    for line in input_file:
        full_list.extend(line.translate(translator).split(' '))
    return full_list


def build_trigram(full_list):
    """
    Here we create the trigram dictionary, the values are pulled from the words
    following the stripped key.
    """
    sherlock_dict = {}
    for i in range(0, len(full_list) - 2):
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        if trigram_key in sherlock_dict:
            sherlock_dict[trigram_key].append(trigram_value)
        else:
            sherlock_dict[trigram_key] = [trigram_value]
    return sherlock_dict


def build_text(word_pairs):
    """
    This is where we take a random key, and hopefully generate sentences.  So,
    the biggest problem I had was bouncing back and forth between dicts, tuples,
    and strings.
    """
    word = random.choice(list(word_pairs.keys()))
    output_text = ""
    text_words = list(word)

    while len(text_words) < 100:
        pair = tuple(text_words[-2:])

        if pair in word_pairs:
            text_words.append(random.choice(word_pairs[pair]))
        else:
            text_words[-1] += "."
            alternate_pair = random.choice(list(word_pairs.keys()))
            text_words.extend(list(alternate_pair))

    output_text = "START\n\n" + " ".join(text_words) + "! \
    \n\nEND"
    return output_text


def main():
    """
    Main run list
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    input_file = parse_file(filename)
    words = make_words(input_file)
    word_pairs = build_trigram(words)
    output_text = build_text(word_pairs)
    print(output_text)

if __name__ == "__main__":
    main()
