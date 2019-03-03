#!/usr/bin/env python3

import math

class Circle():
    """ Circle class """

    def __init__(self, radius):
        self.radius = radius

    def __call__(self):
        return 2 * math.pi * self.radius ** 2


def main():
    c1 = Circle(5)
    c2 = Circle(10)

    print(c1())
    print(c2())

if __name__ == '__main__':
    main()
