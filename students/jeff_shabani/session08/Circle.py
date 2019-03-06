#!/usr/bin/env python3

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.diameter = value

    #@diameter.getter


    def __repr__(self):
        return f'The radius is {self.radius} & diamer is {self.diameter}'


if __name__ =='__main__':
    c = Circle(5)

    print(c)

    c.diameter = 20
    print(c.diameter)