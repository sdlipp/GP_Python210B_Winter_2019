
"""
A class-based system for rendering html.
"""
# This is the framework for the base class

class Element:
    tag = 'html'
    int_count = 0
    def __init__(self,content= None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def att_output(self):
        att_output = []
        for k, v in self.atts.items():
            att_output.append(f'{k}="{v}"')
        return ' '.join(att_output)
            

    def append(self, new_content):
        """appending the contents to the class object"""

        self.content.append(new_content)


    def open_tag(self):
        if self.att_output():
            return f'<{self.tag} {self.att_output()}>'
        else:
            return f'<{self.tag}>'



    def render(self, out_file):

        out_file.write(self.open_tag() + '\n')
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
                out_file.write('\n')
            else:
                line.render(out_file)
        out_file.write(f'</{self.tag}>\n')

        

class Html(Element):
    tag = 'html'

    def open_tag(self):
       return f'<!DOCTYPE {self.tag}>\n<{self.tag}>'
        



