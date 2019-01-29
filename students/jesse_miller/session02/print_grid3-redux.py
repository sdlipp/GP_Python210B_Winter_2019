#!/usr/local/bin/python3
# Asking for user input
n = int(input("Enter a number for the size of the grid: "))
m = int(input("Enter a number for the number of squares: "))

def do_one(f):
    f()
"""This, again, is me not being sure how to just pull a function once in a
function"""

def do_two(f):
    f()
    f()
"""This runs the given function twice"""

def do_row(f):
    for _ in range(n):
        do_one(f)
"""This function is to print a row for every iteration of variable 'n'"""


minus = (' -')
plus = '+'
"""Here, I'm defining the variables for printing.  Made the math easier this
way"""

def print_line():
    print((plus + (minus * n)) * m + plus)
"""This defines the tops and bottoms of the squares"""

def print_post():
    print(('|' + (' ' * (2 * n))) * (m + 1)),
"""This defines the column markers.  The 2*n is to coensate for the length of
the column being double the length of a row in print.  Note that as opposed to
the previous version, padding has been removed from the above two functions to
compensate for adding more squares total"""

def print_row():
    for _ in range(n):
        print_post()
"""This takes the way above function and creates a way to easily iterate it
based off of 'm' """

def print_column(f):
    for _ in range(n):
        print_line()

def print_grid():
    """The remainder of the magic.  It doubles the above function and prints
    the last row"""
    print_line()
    for line in range(m):
        for post in range(n):
            print_post()
        print_line()
print_grid()
