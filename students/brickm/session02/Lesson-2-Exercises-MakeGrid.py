# Lesson: 02 Excercises 
# Title: Make Grid
# Auther: Brick

#first pass
plus_minus_line = '+ - - - - + - - - - +'
bar_line = '|         |         |'

def print_grid_first_pass():
    print(plus_minus_line)
    print(bar_line)
    print(bar_line)
    print(bar_line)
    print(bar_line)
    print(plus_minus_line)
    print(bar_line)
    print(bar_line)
    print(bar_line)
    print(bar_line)
    print(plus_minus_line)

print_grid_first_pass()

#alternate using more functions

def do_once(f):
    f()

def do_four(f):
    f()
    f()
    f()
    f()

def print_plus_minus():
    print(plus_minus_line)

def print_post():
    print(bar_line)
    
def print_grid_second_pass():
    do_once(print_plus_minus)
    do_four(print_post)
    do_once(print_plus_minus)
    do_four(print_post)
    do_once(print_plus_minus)

print_grid_second_pass()

