#!/usr/bin/env python3

import math


class Circle():
    """ Circle class """

    def __init__(self, radius=0):
        self._radius = radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __le__(self, other):
        return self._radius <= other.radius

    def __eq__(self, other):
        return self._radius == other.radius

    def __ge__(self, other):
        return self._radius >= other.radius

    def __gt__(self, other):
        return self._radius > other.radius

    def __ne__(self, other):
        return self._radius != other.radius

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    @property
    def diameter(self):
        return self._radius * 2 

    @diameter.setter
    def diameter(self, value):
        self._radius = .5 * value

    @property
    def area(self):
        return 2 * math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls()
        self._radius = diameter * .5
        return self
