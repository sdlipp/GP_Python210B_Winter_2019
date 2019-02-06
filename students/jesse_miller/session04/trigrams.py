#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import codecs
import random

input_ = []

def open_file():
    """
    I was so overthinking this, I think I've got it now however.  This opens
    the file and throws it into a list.
    """
    with open('sherlock.txt', 'r') as f:
        sherlock_input = f.read()
    cleanString(sherlock_input)

def cleanString(sherlock_input):
    """
    This should strip out everything I don't want, punctuation wise, from the
    file
    """
    newstring = sherlock_input
    newstring = newstring.replace("!","")
    newstring = newstring.replace("@","")
    newstring = newstring.replace("#","")
    newstring = newstring.replace("$","")
    newstring = newstring.replace("%","")
    newstring = newstring.replace("^","")
    newstring = newstring.replace("&","and")
    newstring = newstring.replace("*","")
    newstring = newstring.replace("(","")
    newstring = newstring.replace(")","")
    newstring = newstring.replace("+","")
    newstring = newstring.replace("=","")
    newstring = newstring.replace("?","")
    newstring = newstring.replace("\'","")
    newstring = newstring.replace("\"","")
    newstring = newstring.replace("{","")
    newstring = newstring.replace("}","")
    newstring = newstring.replace("[","")
    newstring = newstring.replace("]","")
    newstring = newstring.replace("<","")
    newstring = newstring.replace(">","")
    newstring = newstring.replace("~","")
    newstring = newstring.replace("`","")
    newstring = newstring.replace(":","")
    newstring = newstring.replace(";","")
    newstring = newstring.replace("|","")
    newstring = newstring.replace("\\","")
    newstring = newstring.replace("/","")
    return sherlock_output
trigram(sherlock_output)


def trigram(sherlock_output):
    """
    This should math and map out the trigram, at least, right now I think it
    will.
    """
    for i in range(len(sherlock_output) - 2):
        trigram_input = tuple(sherlock_output[i:i + 2])
        trigram_fold = sherlock_output[i + 2]
        trigram.setdefault(trigram_input, []).append(trigram_fold)
    return swapped
    create_output(swapped, trigram_input)


def create_output(swapped, trigram_input):
    """
    This should take the trigram mapping and use it against the text of the
    story.  At least, I hope.
    """
    random_number = random.randrange(0, len(swapped))
    for i, trigram_input in enumerate(trigram):
        if i == random_number:
            start_string = trigram_ibput
            break
    output_list = list(start_string) + trigram[start_string]
    return final_output
    print_output(final_output)

def print_output(final_output):



def main():

if __name__ == "__main__":
    main()
