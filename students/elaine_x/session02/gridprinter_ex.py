########################
#Python 210
#Session 02 - Grid Printer
#Elaine Xu
#Jan 21,2019
########################

#Part 1 write a function that draws a grid
#print first two blocks using 'for' loop
for i in range(2):
    print('+'+' -'*4+' +'+' -'*4+' +')
    #print 4 rows of '|'
    for row in range(4):
        print('|'+'  '*4+' |'+'  '*4+' |')
#print last line
print('+'+' -'*4+' +'+' -'*4+' +')


#Part 2 takes one integer argument and prints a grid
def print_grid(n):
    '''print a grid with n number of grid spacing'''
    if n <3 or n%2 != 1:
        print('Invalid input, use an odd number no less than 3')
    else:
        x = int((n-1)/2)
        #print(type(x)) #test
        #print first two blocks using 'for' loop
        for i in range(2):
            print('+'+' -'*x+' +'+' -'*x+' +')
            #print half of '|'
            for i in range(x):
                print('|'+'  '*x +' |'+'  '*x+' |')
        #print last line
        print('+'+' -'*x+' +'+' -'*x+' +')
#test out
print_grid(3)
print_grid(15)


#Part 3 write a function that draws a grid with a specified number of rows and columns
def print_grid2(a,b):
    '''print a grid with number a of blocks in one row and b grid spacing'''
    a = int(a)
    b = int(b)
    if a <= 0 or b <=0:
        print('Invalid number')
    else:
        #'for' loop for number 'a' of blocks
        for i in range(a):
            #print '+' row
            for i in range(a):
                print('+'+' -'*b,end='')
            print(' +')

            #print '|' row
            for i in range(b):
                for i in range(a):
                    print('|'+'  '*b,end='')
                print(' |')
    
        #print last line
        for i in range(a):
            print('+'+' -'*b,end='')
        print(' +')
#test out
print_grid2(3,5)
print_grid2(1,1)