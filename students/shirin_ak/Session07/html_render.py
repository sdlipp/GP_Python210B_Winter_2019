

class Element:
    tag = 'html'
    int_count = 0
    def __init__(self, name ="" content= "", **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = {}



