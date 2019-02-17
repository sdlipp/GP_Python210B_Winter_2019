"""Computing the Fibonacci and Lucas  Numeric Series"""


def fib(n):
    """ compute the nth Fibonacci number """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


print(fib(9))



def luc(n):
    """ compute the nth Lucas number """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return luc(n - 2) + luc(n - 1)


print(luc(9))



def sum_series(n, *args, **kwargs):
    """
        compute the nth value of a summation series.

        Used the *args and **kwargs as an optional parameter to pass arguments after
        the required parameter.

        This function generalizes the fibonacci() and the lucas(),
        so that the function works for any first two numbers for a sum series.
        Sum_series(n, 0, 1) is equivalent to fibonacci(n).
        And sum_series(n, 2, 1) is equivalent to lucas(n).
        """
    f = kwargs.get('f', None)
    s = kwargs.get('s', None)

    if fib == n:
        return fib(9)
    elif luc == n:
        return luc(9)
    else:
        return fib(n - 2) + fib(n - 1)



print(sum_series(fib, 0, 1))
print(sum_series(luc, 2, 1))



""" Series of assert statements to demonstrate the three functions work properly. """


if __name__ == "__main__":
    # run some tests
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13

    assert luc(0) == 2
    assert luc(1) == 1

    assert luc(4) == 7

    assert sum_series(5) == fib(5)

    # test if sum_series matched lucas
    assert sum_series(luc, 2, 1) == luc(9)

    print("tests passed")

