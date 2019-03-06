#!/usr/bin/env python3

class Circle(object):
    def __init__(self, radius):
        self.radius = radius


    @property
    def diameter(self):
        return self.radius *2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    #@diameter.getter


    def __repr__(self):
        return f'The radius is {self.radius} & diamer is {self.diameter}'


# if __name__ =='__main__':
#     c = Circle(5)
#     print(c)
#
#     c.radius=6
#     print(c)
#
#     c.diameter = 40
#     print(c)
