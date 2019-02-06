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
the file and throws it into a list.
    """
    #with open('sherlock_small.txt', 'r') as f:
        #sherlock_input = f.read()
sherlock_input = set(line.strip() for line in open('sherlock_small.txt'))
sherlock_output = None
#    cleanString(sherlock_input)
#print(sherlock_input)
for i in sherlock_input:
    sherlock_input = i.rstrip().translate(str.maketrans(' ', ' ', string.punctuation))
    print(sherlock_input)
    sherlock_output = set.add(sherlock_input)
print(sherlock_input)
#def cleanString(sherlock_input):
"""
This should strip out everything I don't want, punctuation wise, from the
file
"""


#def trigram(sherlock_output):



#def create_output(swapped, trigram_input):


#def print_output(final_output):




#def main():


#if __name__ == "__main__":
#    main()
