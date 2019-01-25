str1 = "+" + (" -" * 4 + " +") * 2
str2 = "|" + " " * 9 + "|" + " " * 9 + "|"

print(str1)
print(str2)
print(str2)
print(str2)
print(str2)
print(str1)
print(str2)
print(str2)
print(str2)
print(str2)
print(str1)

def print_grid(n):
    """Print a square grid with 4 equally sized cells of adjustable size"""
    str1 = "+" + (" -" * n + " +") * 2
    str2 = "|" + (" " * (n * 2 + 1) + "|") * 2

    print(str1)
    for i in range(n):
        print(str2)
    print(str1)
    for i in range(n):
        print(str2)
    print(str1)

print_grid(1)
print_grid(0)

def print_grid2(n, m):
    """Print a square grid with an adjustable number of total cells and size"""
    str1 = "+" + (" -" * n + " +") * m
    str2 = "|" + (" " * (n * 2 + 1) + "|") * m

    for j in range(m):
        print(str1)
        for i in range(n):
            print(str2)
    print(str1)

print_grid2(2,2)
print_grid2(1,1)
print_grid2(0,0)