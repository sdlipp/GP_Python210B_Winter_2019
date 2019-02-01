#!/usr/local/bin/python3


def fizz_buzz():
    """Print 1 - 100 with each number on its own line. Replace multiples of 3 with Fizz. Replace multiples of 5 with Buzz.
    Replace multiples of both 3 and 5 with FizzBuzz."""
    x = 1
    while x < 101:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        x += 1


fizz_buzz()
