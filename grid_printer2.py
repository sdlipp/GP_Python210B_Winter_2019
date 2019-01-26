#Part 2 - make it a function

def print_grid(n):
    x = 0
    y = 0
    plus = '+'
    minus = '-'
    pipe = '|'
    row = (plus + ' -'*n+' ')*2 + plus
    column = (pipe + ' '*(n*2+1))*2+ pipe   
    while x < 2:
        print(row)
        x += 1
        y = 0
        while y < n:
            print(column)
            y += 1
    print(row, end=' ')
    print()