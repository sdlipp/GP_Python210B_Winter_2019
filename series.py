# Fibonacci numbers only
def fibonacci(n):
    """returns the nth value in the fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1       
    else:    
        return (fibonacci(n-2) + fibonacci(n-1))


#Lucas numbers only
def lucas(n):
    """returns the nth value in the lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1       
    else:
        return (lucas(n-2) + lucas(n-1))


#Fibonacci or Lucas series
def sum_series(n,first=0,second=1):
    """returns the nth value in either the fibonacci series or the lucas series depending on which function is called"""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:    
        return (sum_series(n-2, first, second) + sum_series(n-1, first, second))


#Testing using assert statements    

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