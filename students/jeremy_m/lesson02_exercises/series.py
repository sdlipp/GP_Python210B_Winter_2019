# Lesson 02 Exercise: Fibonacci Series
# Jeremy Monroe


def fibonacci(n):
    """ Returns the integer at index n in the fibonacci sequence. """
    if n <= 0:
        return 0
    if n < 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

# print(fibonacci(7))


def lucas(n):
    """ Returns the lucas number at index n """
    if n <= 0:
        return 2
    elif n < 2:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

# print(lucas(4))


def sum_series(n, o=0, p=1):
    """ Returns the integer at index n from a series based on the starting
        numbers specified with parameters o and p. The default settings of these
        parameters result in the fibonacci series """
    if n <= 0:
        return o
    elif n < p + 1:
        return n
    else:
        return sum_series(n - 1, o, p) + sum_series(n - 2, o, p)


# this should return 7, the 4th index in the lucas numbers
# print(sum_series(4, 2, 1))



if __name__ == '__main__':
    assert fibonacci(4) == 3
    assert fibonacci(12) == 144

    assert lucas(4) == 7
    assert lucas(10) == 123

    assert sum_series(6) == fibonacci(6)
    assert sum_series(3, 2, 1) == lucas(3)

    print('All tests passed')