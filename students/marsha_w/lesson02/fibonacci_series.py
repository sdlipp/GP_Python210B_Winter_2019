'''
Title:Fibonacci and Lucas
Dev:Marsha Wheeler
Date:01-23-18
'''

'''Create a new module series.py in the session02 folder in your student folder.
In it, add a function called fibonacci.
The function should have one parameter n.
The function should return the nth value in the fibonacci series (starting with zero index).
Ensure that your function has a well-formed docstring'''
# fibonacci series function
def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n == 0:
        return 0
    else:
        n1 = 0
        n2 = 1
        count = 0
        while count < n:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            if count == n:
                return n1

#lucas series function
def lucas(n):
    """ compute the nth Lucas number """
    if n == 0:
        return 2
    else:
        n1 = 2
        n2 = 1
        count = 0
        while count < n:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            if count == n:
                return n1

def sumSeries(n, n1=0, n2=1):
    """
    compute the nth value of a summation series.
    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n == 0 and n1 == 0:
            return 0
    elif n == 0 and n1 == 2:
        return 2
    else:
        count = 0
        while count < n:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            if count == n:
                return n1

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

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    assert sumSeries(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sumSeries(5, 2, 1) == lucas(5)

    assert sumSeries(0, 2, 1) == lucas(0)
    print("tests passed")
