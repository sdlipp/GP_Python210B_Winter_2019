#!/usr/bin/env python3
import math


class Circle(object):
    instances = []

    def __init__(self, radius):
        self.radius = radius
        Circle.instances.append(self)

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

    def __iadd__(self, other):
        return self.radius + other.radius

    def __ipow__(self, other):
        return self.radius ** other

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


class Sphere(Circle):

    def volume(self):
        return (4/3)*math.pi*(self.radius**3)

    def area(self):
        return 4 * math.pi * (self.radius**2)

    def __repr__(self):
        return f'Sphere with radius of {self.radius} volume of {self.volume()} & surface area of {self.area()}'

    def __str__(self):
        return f'Sphere with radius of {self.radius} volume of {self.volume()} & surface area of {self.area()}'



if __name__ == '__main__':

    c1 = Circle(1)
    c2 = Circle(5)
    c3 = Circle(3)
    c4 = Circle(4)
    c5 = Circle(2)
    s=Sphere(10)
    sfd = Sphere.from_diameter(4)
    print(s)




