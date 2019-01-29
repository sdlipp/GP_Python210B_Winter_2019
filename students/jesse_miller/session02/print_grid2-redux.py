#!/usr/local/bin/python3
# Asking for user input
n = int(input("Enter a number for the size of the grid: "))
minus = (' -' * n)
plus = '+'
"""Here, I'm defining the variables for printing.  Made the math easier this
way"""

def print_line():
    print(plus + minus + plus + minus + plus)
"""This defines the tops and bottoms of the squares"""

def print_post():
    print('|' + (' ' * (2*n) ) + '|' + (' ' * (2*n) ) + '|'),
"""This defines the column markers.  The 2*n is to compensate for the length of
the column being double the length of a row in print"""

def print_grid():
    """The remainder of the magic.  It doubles the above function and prints
    the last row"""
    print_line()
    for line in range(2):
        for post in range(n):
            print_post()
        print_line()
print_grid()
"""This defines the grid function.  It executes print_row twice through do_two,
and the print_line to close the square."""
