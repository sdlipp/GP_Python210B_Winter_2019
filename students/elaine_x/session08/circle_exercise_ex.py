'''
##########################
#Python 210
#Session 07 - Circle Exercise
#Elaine Xu
#Mar 5, 2019
###########################
'''
import math
#############################
#Step 1 create class called circle
#############################
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

#############################
#Step 2 add diameter property
#############################
    @property
    def diameter(self):
        print("in getter")
        return self.radius * 2

#############################
# Step 3 set up diameter property setter
#############################
    @diameter.setter
    def diameter(self, value):
        print("in setter", value)
        self.radius = value / 2

#############################
# Step 4 add an area property
#############################
    @property
    def area(self):
        return math.pi * self.radius**2

#############################
# Step 5 add an alternate constructor that create circle directly with the diameter
#############################

#    @classmethod
#    def from_diameter(cls, diameter):
#        self = cls(self)
#        self.diameter = diameter
#        self.radius = diameter/2
#        return self.diameter


#############################
# Step 6 add __str__ and __repr__ methods
#############################
    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)


#############################
# Step 7 add numerical protocol
#############################
    def __add__(self, other):
        return "Circle({})".format(self.radius + other.radius)

    def __mul__(self, other):
        return "Circle({})".format(self.radius * other)

#############################
# Step 8 add ability to compare two circles
#############################

#############################
# Step 9 sphere subclassing
#############################
'''c = Circle(4)
c = Circle.from_diameter(8)
print(c.diameter)
'''
c1 = Circle(2)
c2 = Circle(4)
print(c1+c2)
print(c2 * 3)
#print(3 * c2)