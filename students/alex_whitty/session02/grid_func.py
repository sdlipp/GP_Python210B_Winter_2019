
"""Wrote several functions that takes one argument and prints a grid."""




def plus():
    plus = '+'
    return plus


def minus(args):
    minus = ' - ' * args
    return minus


def vert_dash(args):
    vert_dash = '|' + ' ' * args + ' | ' + ' ' * args + '|'
    return vert_dash


def print_grid(n):
    print(plus() + minus(1) + plus() + minus(1) + plus())
    print(vert_dash(2))
    print(plus() + minus(1) + plus() + minus(1) + plus())
    print(vert_dash(2))
    print(plus() + minus(1) + plus() + minus(1) + plus())


print_grid(2)


def print_grid(n):
    print(plus() + minus(4) + plus() + minus(4) + plus())
    print(vert_dash(11))
    print(vert_dash(11))
    print(vert_dash(11))
    print(vert_dash(11))
    print(plus() + minus(4) + plus() + minus(4) + plus())
    print(vert_dash(11))
    print(vert_dash(11))
    print(vert_dash(11))
    print(vert_dash(11))
    print(plus() + minus(4) + plus() + minus(4) + plus())


print_grid(11)

def print_grid(n):
    print(plus() + minus(15) + plus() + minus(15) + plus())
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(plus() + minus(15) + plus() + minus(15) + plus())
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(vert_dash(44))
    print(plus() + minus(15) + plus() + minus(15) + plus())


print_grid(44)


