




class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f'The radius is {self.radius}'


if __name__ =='__main__':
    c = Circle(5)
    print(c)