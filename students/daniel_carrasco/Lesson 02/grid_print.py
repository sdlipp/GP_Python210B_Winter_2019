def print_grid(n,x):
    space = n*' - '
    l = ('+'+n*' - ')*x+'+'
    w = ('|'+len(space)*' ')*x+ '|'
    j = 1

    print(l)
    while j<=x:
        k = 1
        while k<=n:
            print(w)
            k+=1
        j+=1
        print(l)

print_grid(4,4)