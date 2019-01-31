#!/usr/bin/env python3

# Douglas Klos
# January 20th, 2019
# Python 210, Assignment 2
# fizzbuzz.py


def fizzbuzz(n=100):
    """ displays fizzbuzz to specified number, defaults to 100 """

    # For loop is not inclusive, so we run it to 101 to include 100.
    for num in range(1, n+1):

        # If the number is divisible by 3, then we print Fizz.
        # We don't want a newline yet, as if it also divisible by 5
        #   we'll add to the line.
        if num % 3 == 0:
            print('Fizz', end='')

        # If the number is divisible by 5, then we print Buzz.
        # While we want a newline always after buzz, it is added after
        #   the conditionals.
        if num % 5 == 0:
            print('Buzz', end='')

        # If the number is neither divisible by 3 nor 5, we print the
        #   number itself.  Still no newline at this point.
        if (num % 3 != 0 and num % 5 != 0):
            print(num, end='')

        # Here's our newline.  This allows the first two if's to work
        #   together in displaying FizzBuzz.
        print()


if __name__ == "__main__":
    fizzbuzz(10)
    fizzbuzz(100)
