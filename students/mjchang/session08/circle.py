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
        return self.radius**2 * math.pi
    