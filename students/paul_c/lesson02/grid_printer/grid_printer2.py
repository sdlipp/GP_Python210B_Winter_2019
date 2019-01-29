#!/usr/local/bin/python3


def grid(x):
    """
    Create a 2 by 2 grid of varying size.

    :param: arg1: x determines the size of the grid by adding segments to each box side.
    """
    for i in range(2):
        row = "+" + " - " * x
        print(row, row, "+")
        column = "|" + " " * (x * 3)
        for i in range(x):
            print(column, column, "|")
    print(row, row, "+")


grid(10)  # 10 was chosen arbitrarily. It can be replaced with any number.
