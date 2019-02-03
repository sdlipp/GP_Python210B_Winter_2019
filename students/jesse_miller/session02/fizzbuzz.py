#!/usr/local/bin/python3
for i in range(1,101):
    string = ""
    if i % 3 == 0:
        string = string + "Fizz"
    if i % 5 == 0:
        string = string + "Buzz"
    if i % 5 != 0 and i % 3 != 0:
        string = string + str(i)
    print(string)
