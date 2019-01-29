#!/usr/local/bin/python3
def exchange_first_last(seq):
    if len(seq) <= 1:
        return seq
    mid = seq[1:len(seq)-1]
    return seq[len(seq)-1] + mid + seq[0]


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

assert every_other_removed(a_string) == "agia a tig htscoe"
print("Test Passed - every other removed")

assert exchange_first_last(a_string) == "e guitar has strings that's closa"
print("Test Passed - first and last letters exchanged")
