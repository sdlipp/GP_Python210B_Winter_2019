#print('+','-'). adds a space between + and -
#print('+' + '-') same as ('+'+'-'). does not add space between + and -

#print('+', end=' ')
#print('-')

#print(plus+4*' -', plus+4*' -', plus)
#print(plus+4*minus, plus+4*minus, plus) same thing as above if you define ' -' as minus and '+' as plus

#print('|'+8*' ', '|'+8*' ', '|')
#print(line+8*space, line+8*space, line) same thing as above if you define '|' as line and ' ' as space


#method 1
print('+'+4*' -','+'+4*' -','+')
print('|'+8*' ', '|'+8*' ', '|')
print('|'+8*' ', '|'+8*' ', '|')
print('|'+8*' ', '|'+8*' ', '|')
print('+'+4*' -','+'+4*' -','+')
print('|'+8*' ', '|'+8*' ', '|')
print('|'+8*' ', '|'+8*' ', '|')
print('|'+8*' ', '|'+8*' ', '|')
print('|'+8*' ', '|'+8*' ', '|')
print('+'+4*' -','+'+4*' -','+')

#method 2
plus = '+'
minus = ' -'
line = '|'
space = ' '
print(plus+4*minus,plus+4*minus,plus)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(plus+4*minus,plus+4*minus,plus)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(line+8*space,line+8*space,line)
print(plus+4*minus,plus+4*minus,plus)

#PART 2

plus = '+'
minus = ' -'
line = '|'
space = ' '
indent = '\n'
x = 4
y = 8

def print_grid():
    string1=plus+x*minus,plus+x*minus,plus+indent
    string2=line+y*space,line+y*space,line+indent
    print(string1+string2*4+string1+string2*4+string1)

##def print_grid(n, x, y):
##    if n==11:
##        return x==4 and y==8
##    elif n<11:
##        return x<4 and y<8
##    else n>11:
##        return x>4 and y>8
    
#stuck with this function

