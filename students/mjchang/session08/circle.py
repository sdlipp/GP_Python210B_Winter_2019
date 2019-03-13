#!/usr/bin/env python3

"""
Circle class exercise
"""
import math

#### Step 1 - create Circle class with the radius ####
class Circle(object):
    def __init__(self, radius):
        self.radius = radius


#### Step 2 - add diameter ####
    @property
    def diameter(self):
        return self.radius * 2


#### Step 3 - diameter property ####
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2


#### Step 4 - add area property ####
    @property
    def area(self):
        return math.pi * self.radius**2


#### Step 5 ####
    """
    add alt constructor w/ class method to create circle w/ specified diameter
    """
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)


#### Step 6 - add __str__ and __repr__ methods ####
    def __str__(self):
        return "Circle with radius: {}".format(str(self.radius))

    def __repr__(self):
        return "Circle({})".format(self.radius)


#### Step 7 - add numerical protocol ####
    def __add__(self, other):
        return self.radius + other.radius

    def __rmul__(self, val):
        return self.radius * val

    def __mul__(self, val):
        try:
            return self.radius * val
        except TypeError:
            rmul(self, val)
            

