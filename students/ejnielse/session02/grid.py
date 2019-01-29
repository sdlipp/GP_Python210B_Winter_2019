#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

# Static, Non-General function
def gridA():
    lat = str('- - - -')
    ver = str('       ')
    print('+', lat, '+', lat, '+')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('+', lat, '+', lat, '+')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('|', ver, '|', ver, '|')
    print('+', lat, '+', lat, '+')

# Funtion with One Parameter
def print_grid(n):
    # Parameter must be an odd integer
    n = int((n-1)/2)
    lat = '+' + str(' - ') * n + '+' + str(' - ') * n + '+'
    ver = '|' + str('   ') * n + '|' + str('   ') * n + '|'
    print(lat)
    for i in range(n):
        print(ver)
    print(lat)
    for i in range(n):
        print(ver)
    print(lat)

# Function with Two Parameters
def print_grid2(m,n):
    # Round Parameters to Nearest Integer
    m = int(round(m,0))
    n = int(round(n,0))
    lat = ('+' + str(' - ') * n)* m + '+'
    ver = ('|' + str('   ') * n)* m + '|'
    print(lat)
    for i in range(m):
        for i in range(n):
            print(ver)
        print(lat)
