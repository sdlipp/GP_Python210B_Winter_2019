
import math
class Circle():
    def __init__(self, radius):
        # STEP 1 The radius is a required parameter
        self.radius = radius
    # STEP 2 Add a 'diameter' property
    @property
    def diameter(self):        
        return self.radius*2
    
    #STEP 3 set up the diameter property
    @diameter.setter
    def diameter(self, value):
        self.diameter = value
        self.radius = value/2
        
    #STEP 4 Add an area property
    @property    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # STEP 5 Add an “alternate constructor” that
    #lets the user create a Circle directly with the diameter:
    @classmethod
    def from_diameter(class_object, diameter):
        radius = diameter/2
        return class_object(radius)
        
    #STEP 6 Add __str__ and __repr__ methods to your Circle class.
    
    def __str__(self): 
        return "Circle with radius: {:.6f}".format(self.radius) 

    def __repr__(self): 
        return "Circle({r})".format(r=self.radius) 
   #STEP 7 Add two circles and multiply one by a number
    def ___add__(self, other):
        c1 = self.radius
        c2 = other.radius
        return Circle(c1+c2)
#    def __mul__(self, other):




