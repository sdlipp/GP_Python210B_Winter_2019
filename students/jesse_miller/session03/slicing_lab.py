#!/usr/local/bin/python3
#This function swaps the first and last characters in the tuple.  It works by
#slicing the last character, adding position 1 through one back from last, and
#then adding the first character.  All placed into the result variable.
def exchange_first_last(seq):
    result = seq[-1:] + seq[1:-1] + seq[0:1]
    return result

#This will take the string and remove every other character, including spaces.
#The slice here starts at 0 and slices out every second character.
def every_other_removed(seq):
    result = seq[::2]
    return result
#This function slices out the first four, and four from the last characters
def first_last_four(seq):
    result = seq[4:-4]
    return result
#The :: operand reverses the output, starting at the last position of the tuple
def reversed(seq):
    result = seq[::-1]
    return result

def first_last_middle(seq):
    return a_new_sequence

a_string = "a guitar has strings that's close"
a_tuple = (2, 54, 13, 12, 5, 32, 3, 82, 1)

assert exchange_first_last(a_tuple) == (1, 54, 13, 12, 5, 32, 3, 82, 2)
print("Test Passed - first and last numbers exchanged")

assert every_other_removed(a_string) == "agia a tig htscoe"
print("Test Passed - every other removed")

assert first_last_four(a_string) == "itar has strings that's c"
print("Test Passed - first and last four characters removed")

assert reversed(a_tuple) == (1, 82, 3, 32, 5, 12, 13, 54, 2)
print("Test Passed - tuple reversed")
