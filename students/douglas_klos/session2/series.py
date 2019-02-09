#!/usr/bin/env python3

# Douglas Klos
# January 20th, 2019
# Python 210, Assigment 2
# series.py


def fibonacci(n):
    """
    recursively computes the nth Fibonacci number
    fib(n) = fib(n-2) + fib(n-1)
    """
    if (n <= 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """
    recursively computes the nth Lucas number
    lucas(n) = lucas(n-2) + lucas(1).
    when n == 0, lucas = 2 and when n == 1, lucas = 1
    """
    if (n == 0):
        return 2
    if (n == 1):
        return 1
    return lucas(n-2) + lucas(n-1)


def sum_series(n, n0=0, n1=1):
    """
    recursively computes the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    This way, if no arguments are passed, it defaults to a Fibonacci sequence.

    This function generalizes the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    """

    if (n == 0):
        return n0
    if (n == 1):
        return n1
    return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)


if __name__ == "__main__":
    """ series.main """

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, n1=1, n0=0) == fibonacci(5)
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
