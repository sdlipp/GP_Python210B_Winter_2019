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
    This should math and map out the trigram
    """
    for i in range(len(sherlock_output) - 2):
        trigram_input = tuple(sherlock_output[i:i + 2])
        trigram_fold = sherlock_output[i + 2]
def main():

if __name__ == "__main__":
    main()
