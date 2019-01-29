'''
Title:Grid Printer Exercise
Dev:Marsha Wheeler
Date:01-23-18
'''

#Write a function that draws a Grid and uses two parameters in the function
def drawGrid(nRows, nCells):
    plus = '+'
    minus = '-'
    bar = '|'
    line1 = plus + minus * nCells + plus + minus * nCells + plus # concatenate strings
    line2= bar +' ' * nCells + bar +' ' * nCells + bar # concatenate strings
    for i in range(0,nRows):
        print(line1)
        for i in range(0, nCells):
            print(line2)
    print(line1)


drawGrid(3,3)
