#!/usr/bin/env python3
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * pow(self.radius, 2)

    @classmethod
    def from_diameter(cls, value):
        radius = value / 2
        return cls(radius)

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __repr__(self):
        return f'Circle with radius of {self.radius}'

    def __str__(self):
        return f'Circle with radius of {self.radius}'


if __name__ =='__main__':
    c = Circle(5)
    print(c)
    #del c

    c.radius=6
    print(c)
    #del c


    c.diameter = 40
    print(c)
    del c

    nc = Circle.from_diameter(2)
    print(nc)
    print(repr(nc))

    c2 = Circle(2)
    print(nc + c2)
    print(nc * 3)
    print(3 * nc)
    del nc
    c1 = Circle(5)
    c3 = Circle(5)
    print(c1 < c2)
    print(c2 * c1)
    print(c2 != c1)


