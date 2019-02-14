def print_grid(n,x):
    space = x*' - '
    l = ('+'+x*' - ')*n+'+'
    w = ('|'+len(space)*' ')*n+ '|'
    j = 1

    print(l)
    while j<=n:
        k = 1
        while k<=x:
            print(w)
            k+=1
        j+=1
        print(l)

print_grid(5,4)