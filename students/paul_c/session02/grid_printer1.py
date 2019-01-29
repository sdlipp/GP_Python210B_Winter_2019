#!/usr/local/bin/python3


def grid():
    """Create a 2 by 2 grid without passing parameters."""
    for i in range(2):
        row = "+" + " - " * 4
        print(row, row, "+")
        column = "|" + " " * 12
        for i in range(4):
            print(column, column, "|")
    print(row, row, "+")


grid()