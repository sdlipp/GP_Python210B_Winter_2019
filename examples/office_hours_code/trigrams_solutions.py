"""
Implements one possible solution for the trigram problem
"""
#!/usr/local/bin/python3
import string
import random
import sys


def parse_file(filename):
    """
    Parses the source filename
    """
    full_list = []
    translator = str.maketrans('', '', string.punctuation)
    with open(filename) as input_file:
        for line in input_file:
            # Remove carriage return
            line = line.rstrip()
            # Remove punctuation and add to full list
            full_list.extend(line.translate(translator).split(' '))
    return full_list

def build_trigram(full_list):
    """
    Builds a dictionary with 2-element tuples as key and a list of
    words as value.
    """
    trigrams = {}
    for i in range(0, len(full_list) - 2):
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        if trigram_key in trigrams:
            trigrams[trigram_key].append(trigram_value)
        else:
            trigrams[trigram_key] = [trigram_value]
    return trigrams


def build_text(trigrams, word_target):
    """
    Builds a random text using the trigrams dictionary
    """

    next_key = random.choice(list(trigrams.keys()))
    word_list = trigrams[next_key]
    word = random.choice(word_list)
    output_text = ' '.join(next_key) + ' ' + word

    word_count = 3

    while word_count < word_target:
        next_key = (next_key[1], word)

        if next_key in trigrams:
            word_list = trigrams[next_key]
            word = random.choice(word_list)
            output_text += ' ' + word
            word_count += 1
        else:
            break
    return output_text


def main():
    """
    Main program flow
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    words = parse_file(filename)
    trigrams = build_trigram(words)
    output_text = build_text(trigrams, 300)
    print(output_text)

if __name__ == "__main__":
    main()
