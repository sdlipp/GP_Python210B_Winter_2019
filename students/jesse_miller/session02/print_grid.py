#!/usr/local/bin/python3

def do_two(f):
    """This will execute two of the give function"""
    f()
    f()

def do_four(f):
    """This in turn executes four"""
    do_two(f)
    do_two(f)

def print_line():
    """Definition of the lines"""
    print('+ - - - - + - - - - +'),

def print_post():
    """Definition of the columns"""
    print('|         |         |'),

def print_row():
    """This is where the magic starts.  It prints one line and four columns"""
    print_line()
    do_four(print_post)

def print_grid():
    """The remainder of the magic.  It doubles the above function and prints the last row"""
    do_two(print_row)
    print_line()

print_grid()
