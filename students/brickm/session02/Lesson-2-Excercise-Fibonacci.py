# Lesson: 02 Excercises 
# Title: Fibonacci Series Excercise
# Author: Brick

def fibo(n):
    ''' Calculates the Fibonacci number at a given index '''
    if n < 0:
        return None
    # starting values for Fibonacci number series
    a = 0
    b = 1
    #first two members of the series
    series = [a,b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

def lucas(n):
    ''' Calculates the Lucas number at a given index '''
    if n < 0:
        return None
    # starting values for Lucas number series
    a = 2
    b = 1
    #first two members of the series
    series = [a,b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

def general_sum(n, y=0,z=1):
    ''' Calculates the series at a given index '''
    if n < 0:
        return None
    a = y
    b = z
    #first two members of the series
    series = [a,b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

if __name__ == "__main__":
    '''assert test to check general sum matches fibo and lucas output'''
    assert general_sum(3) == fibo(3)
    assert general_sum(3,2,1) == lucas(3)
    print("assertion test passed")