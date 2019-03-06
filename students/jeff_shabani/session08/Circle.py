#!/usr/bin/env python3
import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius


    @property
    def diameter(self):
        return self.radius *2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * pow(self.radius,2)

    @classmethod
    def from_diameter(cls, value):
        radius = value / 2
        return cls(radius)

    def __repr__(self):
        return f'The radius is {self.radius} & diamer is {self.diameter}. Area ist {self.area}'


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

