#!/usr/local/bin/python3
import sys
#"""import sys for .argv input"""
#n = int(sys.argv[1])
"""Realized once I worked through sum_series that I actually didn't need user
input"""

def fibonacci(n):
   """This is a recusive loop to calc the sequence.  The initial test is to make
   certain that the initial number is starting with 1.  From there it calculates
   the sequence"""
   if n <= 1:
	   return n
   else:
	   return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """This is a recusive loop to calc the sequence.  It tests to make certain
    that the n value is not less than zero, if it is zero it becomes 2, and
    if the n value is 1 it returns 1.  From that point, it follows the same
    sequence as fibonacci to run the simple calc"""
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))


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
#    if n < 0:
#        return None
#    elif n == 0:
#        return n0
#    elif n == 1:
#        return n1
#    else:
#        return sum_series(n - 1, n0 , n1) + sum_series(n - 2, n0 , n1)
#    pass

    sum = n0
    if n < 0:
        sys.exit("We are trying to find n less than 0 which is bad.")
    elif n == 0:
        return sum
    else:
        n -= 1
        sum = sum + n1
        return sum_series(n, n1, sum)

"""So, at first I couldn't wrap my head around what was being asked here.  I
ended up talking with a friend who helped me figure out what the request was.
What I ended up doing was taking the same if/elif hirarchy I used for lucas,
and adapting it to here.  I'm almost positive that there's a better way to
write all of this, but I'm still sort of wrapping my brain around Python's
seemingly simpler logic.

Edit: Later I played and found a shorter code brick that also works."""

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

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
