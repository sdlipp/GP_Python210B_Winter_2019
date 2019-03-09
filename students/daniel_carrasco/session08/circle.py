import math
class Circle:
    pi = math.pi
    def __init__(self,the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @property
    def area(self):
        return self.pi*(self.radius)**2

    @area.setter
    def area(self, diameter):
        if input:
            print('Attribute Error') # How do I do this correctly

    @classmethod
    def from_diameter(cls, diameter):
        return Circle(diameter/2)

    def __str__(self):
        return f'circle with a radius of {self.radius}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.radius!r})')

    def __add__(self, c2):
        print(f'Summing {self} + {c2}')
        print(c2.radius)
        return Circle(self.radius+c2.radius)

    def __mul__(self, other):
        return Circle(self.radius*other)

    def __rmul__(self, other):
        return Circle(self.radius*other)

    def __iadd__(self, other):
        return Circle(self.radius+other)
    def __imul__(self, other):
        return Circle(self.radius*other)

    def __lt__(self, other):
        if self.radius < other.radius:return True
        else: return False
    def __le__(self, other):
        if self.radius <= other.radius:return True
        else: return False
    def __eq__(self, other):
        if self.radius == other.radius:return True
        else: return False
    def __ne__(self, other):
        if self.radius != other.radius:return True
        else: return False
    def __gt__(self, other):
        if self.radius > other.radius:return True
        else: return False
    def __ge__(self, other):
        if self.radius >= other.radius:return True
        else: return False



c1 = Circle(2)
c2 = Circle(2)
a = c1 + c2
print(a)
print(c1 == c2)
circles =[Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
circles.sort()
print(circles)
b = Circle(5)
b+=1
print(b)
b*=2
print(b)