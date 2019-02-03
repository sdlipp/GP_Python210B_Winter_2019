#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        if  i % 3 == 0:
            print("Fizz")
        else:
            if  i % 5 == 0:
                print("Buzz")
            else:
                print(i)
