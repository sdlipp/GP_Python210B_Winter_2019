#!/usr/local/bin/python3
"""
Trigrams attempt
"""
import string
import random
import os
import re


#def open_file():
"""
I was so overthinking this, I think I've got it now however.  This opens
the file and throws it into a list, as well as strips punctuation.
"""
sherlock_input = set(line.strip() for line in open('sherlock_small.txt'))
for i in sherlock_input:
    sherlock_input = i.rstrip().translate(str.maketrans(' ', ' ',\
    string.punctuation))
    print(sherlock_input)
#munge_file(sherlock_input)









#def main():


#if __name__ == "__main__":
#    main()
