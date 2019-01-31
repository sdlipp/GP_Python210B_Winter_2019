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

if __name__ == '__main__':
    assert lucas(5, 2, 1) == 11
    assert lucas(5) == 5
    assert fibonacci(7) == 13