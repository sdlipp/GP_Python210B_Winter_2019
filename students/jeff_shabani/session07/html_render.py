#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        if content:
            self.content = content
        else:
            self.content = ''

    def append(self, new_content):
        result = list()
        result.append(new_content)
        for i in result:
            self.content +=i
        return self.content


    def render(self, out_file):
        outtext = f'<html>\n{self.content}\n</html>'
        out_file.write(outtext)

e=Element('Erst Line')
e.append('\nWulliam\nB')
with open('test.html', 'w') as outf:
    e.render(outf)
print(e.content)

