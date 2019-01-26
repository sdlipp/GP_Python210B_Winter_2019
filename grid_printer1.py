#Part 1 - printing a 2x2 grid

plus = '+'
minus = '-'
pipe = '|'
row = (plus+" "+(minus + " ")*4)
column = (pipe + " "*(4*2)+" ")

x = 0
while x < 2:
    print(row*2+plus)
    x += 1
    y = 0
    while y < 4:
        print(column*2+pipe)
        y += 1

print(row*2+plus, end=' ')
print()


