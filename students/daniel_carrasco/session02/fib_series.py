def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)
def sum_series(n,a=0,b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:

        return sum_series(n-1,a,b)+sum_series(n-2,a,b)

print(fibonacci(4))
print(lucas(4))
print(sum_series(4,0,1))

