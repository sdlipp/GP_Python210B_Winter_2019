#!/usr/local/bin/python3
"""This is a test to make sure I understand how the code works."""
import sys
"""import sys for .argv input"""
n = int(sys.argv[1])

def lucas(n):
    """This is a recusive loop to calc the sequence"""
    if n <= 1:
        return n
    else:
        return(lucas(n-1) + lucas(n-2))

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if n <= 0:
    print("Plese enter a positive integer")
else:
    print("lucas sequence:")
    for i in range(n):
        print(lucas(i))
