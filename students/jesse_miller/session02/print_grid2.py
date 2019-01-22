#!/usr/local/bin/python3
import sys
"""Above I'm importing sys for arguments"""
#from argparse import ArgumentParser
#parser = ArgumentParser(description='print_grid3.py X')
#parser.add_argument(' ', choices=['x'], default='h',
#    help="X is size of square.")
#parser.parse_args()
"""This is a bit disappointing.  I wanted to add a help argument for clarity, but I wasn't able to get it to work"""

n = int(sys.argv[1])
"""This is the input variable.  This number determines the length and width of each square in the grid"""

def do_one(f):
    f()
"""This is me not being sure how to just pull a function once in a function"""

def do_two(f):
    f()
    f()
"""This runs the given function twice"""

def do_row(f):
    for _ in range(n):
        do_one(f)
"""This function is to print a row for every iteration of variable 'n'"""

minus = (' -' * n)
plus = '+'
"""Here, I'm defining the variables for printing.  Made the math easier this way"""

def print_line():
    print(plus + minus + plus + minus + plus)
"""This defines the tops and bottoms of the squares"""

def print_post():
    print('|' + (' ' * (2*n) ) + '|' + (' ' * (2*n) ) + '|'),
"""This defines the column markers.  The 2*n is to coensate for the length of the column being double the length of a row in print"""

def print_row():
    print_line()
    do_row(print_post)
"""And here's the magic.  In this function I'm calling on print_line as well as parsing print_post through do_row"""

def print_grid():
    do_two(print_row)
    print_line()
"""This defines the grid function.  It executes print_row twice through do_two, and the print_line to close the square."""

print_grid()
"""Here we execute the whole mess above"""
