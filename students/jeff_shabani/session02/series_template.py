#!/usr/bin/env python3

"""
a template for the series assignment
"""


def sum_series(n, *args):
    """returns nth fibonacci if no args"""
    """else nth lucas if args are 2 and 1"""
    count = 0
    a, b  = int(), int()
    if args:
        a, b = args
    else:
        a, b = 0, 1
    while count < n:
        a, b = b, a + b
        count += 1
    if count == n:
        return a

def fibonacci(n):
    return sum_series(n)

def lucas(n, *args):
    return sum_series(n, *args)

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0,2,1) == 2
    assert lucas(1,2,1) == 1

    assert lucas(4,2,1) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5,2,1)

    print("tests passed")
