#!/usr/bin/env python3
'''
Class based circle calculation exercise
'''

from math import pi
'''
Imported the math module for calculation
'''

class Circle(object):
    '''
    Defining the circle class
    '''
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        '''
        Defining diameter, I think I'm doing this right.
        '''
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        '''
        This seems like the right time to use a setter
        '''
        self.radius = value / 2

    @property
    def area(self):
        '''
        Defining area, I'm a tad more confident in this one
        '''
        return pi * self.radius**2
