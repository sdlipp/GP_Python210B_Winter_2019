#!/usr/local/bin/python3
#This function swaps the first and last characters in the tuple.
def exchange_first_last(seq):
    seq = seq[-1:] + seq[1:-1] + seq[0:1]
    return seq

#This will take the string and remove every other character, including spaces.
def every_other_removed(seq):
    result = ""
    for i in range(len(seq)):
        if i % 2 == 0:
            result = result + seq[i]
    return result

def first_last_four(seq):
    return a_new_sequence

def reversed(seq):
    return a_new_sequence

def first_last_middle(seq):
    return a_new_sequence

a_string = "a guitar has strings that's close"
a_tuple = (2, 54, 13, 12, 5, 32, 3, 82)

assert exchange_first_last(a_tuple) == (82, 54, 13, 12, 5, 32, 3, 2)
print("Test Passed - first and last numbers exchanged")

assert every_other_removed(a_string) == "agia a tig htscoe"
print("Test Passed - every other removed")
