#!/usr/local/bin/python3
import sys
"""Above I'm importing sys for arguments"""
#from argparse import ArgumentParser
#parser = ArgumentParser(description='print_grid3.py X Y')
#parser.add_argument(' ', choices=['x', 'y'], default='h',
#    help="X is size of square, Y is number of squares.")
#parser.parse_args()
"""This is again disappointing.  I wanted to add a help argument for clarity, but I wasn't able to get it to work"""

n = int(sys.argv[1])
m = int(sys.argv[2])
"""These are the input variables.  This numbers determine the length and width of each square in the grid, as well as the number of squares"""

def do_one(f):
    f()
"""This, again, is me not being sure how to just pull a function once in a function"""

def do_two(f):
    f()
    f()
"""This runs the given function twice"""

def do_row(f):
    for _ in range(n):
        do_one(f)
"""This function is to print a row for every iteration of variable 'n'"""

def do_line(f):
    for _ in range(n):
        do_one(f)
"""This does the same as above, except with columns.  I learned a bit from this, but resisted the urge to go back and edit the previous version"""

minus = (' -')
plus = '+'
"""Here, I'm defining the variables for printing.  Made the math easier this way"""

def print_line():
    print((plus + (minus * n)) * m )
"""This defines the tops and bottoms of the squares"""

def print_post():
    print(('|' + (' ' * (2 * n))) * (m + 1)),
"""This defines the column markers.  The 2*n is to coensate for the length of the column being double the length of a row in print.  Note that as opposed to the previous version, padding has been removed from the above two functions to compensate for adding more squares total"""

def print_row():
    do_row(print_post)
"""This takes the way above function and creates a way to easily iterate it based off of 'm' """

def print_grid():
    print_line()
    for _ in range(m):
        print_row()
        print_line()
"""Here we define the process for printing the grid.  Each square is defined by 'n' and printed 'm' number of times"""

print_grid()
