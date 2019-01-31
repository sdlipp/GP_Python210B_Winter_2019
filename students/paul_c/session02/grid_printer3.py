#!/usr/local/bin/python3


def grid(x, y):
    """
    Create a grid with 5x5 boxes. Box sides are segmented into 5 characters.

    :param arg1: x determines how many boxes will be in the grid. This prints as x * x number of boxes.
    :param arg2: y determines how many segments each box gets for its sides.
    """
    for i in range(x):
        row = "+" + " - " * y
        print(row * x + "+")
        for i in range(y):
            column = ("|" + (" " * y * 3)) * (x + 1)
            print(column)
    print(row * x + "+")


grid(5,5)  # 5,5 was chosen arbitrarily. They can be replaced with any numbers.


