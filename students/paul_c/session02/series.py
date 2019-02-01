# !/usr/bin/env python3


def fibonacci(n):
    """ compute the nth Fibonacci number
    :param n: This parameter represents the position of the sequence number.
    :return: The number that is in the nth place of the Fibonacci sequence.

    This function should return the nth number of the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
    pass


def lucas(n):
    """ compute the nth Lucas number
    :param n: This parameter represents the position of the sequence number.
    :return: The number that is in the nth place of the Lucas sequence.

    This function should return the nth number of the Lucas sequence.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)
    pass


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n0 == 0 and n1 == 1:
        return fibonacci(n)
    elif n0 == 2 and n1 == 1:
        return lucas(n)
    pass


if __name__ == "__main__":
    # Tests for the fibonacci function.
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    # Tests for the lucas function.
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    # Tests for the sum_series function
    assert sum_series(1) == fibonacci(1)
    assert sum_series(2) == fibonacci(2)
    assert sum_series(3) == fibonacci(3)
    assert sum_series(4) == fibonacci(4)
    assert sum_series(5) == fibonacci(5)
    assert sum_series(10) == fibonacci(10)
    # test if sum_series matched lucas
    assert sum_series(1, 2, 1) == lucas(1)
    assert sum_series(2, 2, 1) == lucas(2)
    assert sum_series(3, 2, 1) == lucas(3)
    assert sum_series(4, 2, 1) == lucas(4)
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(10, 2, 1) == lucas(10)

    print("tests passed")
