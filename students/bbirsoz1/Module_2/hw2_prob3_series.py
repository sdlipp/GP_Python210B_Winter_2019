
'''
Fibonacci Series
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...
'''

#method 1

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

#self test below
#print (fibonacci(8))

'''
Lucas Series
2, 1, 3, 4, 7, 11, 18, 29, 47, 76...
'''

def lucas(n):
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

#self test below
#print (lucas(8))

'''
Sum Series
'''

def sum_series(n, n0=0, n1=1):
    if n < 0:
        return None
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)
#self test below
#print (sum_series(8, 2, 1))

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
