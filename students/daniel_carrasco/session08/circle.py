class Circle():

    def __init__(self,the_radius):
        self.radius = the_radius
        self.diameter = self.radius*2


c = Circle(4)
print(c.radius)
print(c.diameter)