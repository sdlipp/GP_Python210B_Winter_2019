"""Wrote a function that takes two arguments and prints a grid"""


def plus():
    plus = '+'
    return plus


def minus(m, args):
    minus = ' - ' * args
    return minus


def vert_dash(v, args):
    vert_dash = '|' + ' ' * args + ' | ' + ' ' * args + '|'
    return vert_dash


def print_grid(v, m):
    print(plus() + minus(1, 1) + plus() + minus(1, 1) + plus())
    print(vert_dash(2, 2))
    print(plus() + minus(1, 1) + plus() + minus(1, 1) + plus())
    print(vert_dash(2, 2))
    print(plus() + minus(1, 1) + plus() + minus(1, 1) + plus())




print_grid(2,1)



"""

Tried the nested for loop to reduce the number of print statements.
However, I could not get the align correct to complete all four sides
of the grid at once during execution. 




def print_grid(v, m):
    for i in range(2):
        for i in range(1):
            print(plus() + minus(1) + plus() + minus(1) + plus())
        print(vert_dash(2))


print_grid(2,1)

"""