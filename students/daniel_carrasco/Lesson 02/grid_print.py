def print_grid(n):
    i = int(n/2)
    space = i*' - '
    l = ('+'+i*' - ')*2+'+'
    print(l)
    w = ('|'+len(space)*' '+'|'+len(space)*' '+'|\n')*i
    print(w)
    print(l)
    print(w)
    print(l)
print_grid(15)