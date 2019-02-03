#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

# Funtion to Return the nth Value in the Fibonacci Sequence
def fibonacci(n):
    """Returns the nth value in the Fibonacci Sequence."""
    # n must be a positive integer
    n = abs(int(round(n,0)))
    x = 0
    i = 0
    y = 1
    if n == 0:
        #print("Function Parameter Cannot be Zero")
        return 0
    else:
        while i < n:
            j = x + y
            x = y
            y = j
            i += 1
    #print("The value for term ",n, " in the Fibonacci sequence is:", x)
    return x
    pass

# Funtion to Return the nth Value in the Lucas Numbers Series
def lucas(n):
    """Returns the nth value of the Lucas Numbers Series."""
    # n must be a positive integer
    n = abs(int(round(n,0)))
    x = 2
    i = 0
    y = 1
    if n == 0:
        #print("Function Parameter Cannot be Zero")
        return 2
    else:
        if n == 1:
            return 1
        else:
            while i < n:
                j = x + y
                x = y
                y = j
                i += 1
    #print("The value for term ",n, " in the Lucas Series is:", x)
    return x
    pass

#Funtion to Return the nth Value in User Defined Recursive Number Series
def sum_series(n, first_val=None, second_val=None):
    """
    Returns the nth value of an additive recursive number series in which
    the user defines the first two values.
    """
    # n must be a positive integer
    n = abs(int(round(n,0)))
    first_val = first_val or 0
    i = 0
    second_val = second_val or 1
    if n == 0:
        #print("n Parameter Cannot be Zero")
        return first_val
    else:
        if n == 1:
            return second_val
        else:
            return sum_series(n-2, first_val, second_val) + sum_series(n-1, first_val, second_val)
    #print("The value for term ",n, " in the Sum_Series is:", first_val)
    pass

if __name__ == '__main__':
    # Run Some Tests
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

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
