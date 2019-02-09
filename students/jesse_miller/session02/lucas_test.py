#!/usr/local/bin/python3
"""This is a test to make sure I understand how the code works."""
import sys
"""import sys for .argv input"""
n = int(sys.argv[1])

def lucas(n):
    """This is a recusive loop to calc the sequence"""
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))

if n <= 0:
    print("Plese enter a positive integer")
else:
    print("lucas sequence:")
    for i in range(n):
        print(lucas(i))
