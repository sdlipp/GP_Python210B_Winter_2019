#!/usr/local/bin/python3
def print_line():
    """Definition of the lines"""
    print('+ - - - - + - - - - +'),

def print_post():
    """Definition of the columns"""
    print('|         |         |'),

def print_row():
    """This is where the magic starts.  It prints one line and four columns"""
    print_line()
#    do_four(print_post)

def print_grid():
    """The remainder of the magic.  It doubles the above function and prints
    the last row"""
    print_line()
    for line in range(2):
        for post in range(4):
            print_post()
        print_line()
print_grid()
