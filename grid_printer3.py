#Part 3 - a function with two parameters

def print_grid2(count, size):
    x = 0
    plus = '+'
    minus = '-'
    pipe = '|'
    row = (plus+" "+(minus + " ")*size)
    column = (pipe + " "*(size*2+1))
    while x < count: 
        print(row*count+plus)
        x += 1
        y = 0
        while y < size:   
            print(column*count+pipe)
            y += 1
    print(row*count+plus, end=' ')
    print()