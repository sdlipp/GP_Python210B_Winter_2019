def horz(a,b):
    cross = '+' + '-'*b
    print(cross *a+'+')

def vert(n,k):
    print('|'.ljust(n+1)*(k+1))

def grid(a,b):
    for k in range(a):
        horz(a,b)
        for i in range(b):
            vert(b,a)
    horz(a,b)

print(grid(2,3))