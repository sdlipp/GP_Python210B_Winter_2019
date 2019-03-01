#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None, tag=None):
        if tag:
            self.tag = tag
        else:
            self.tag = ''
        if content:
            self.content = content
        else:
            self.content = ''


    def append(self, new_content):
        result = list()
        result.append(new_content)
        for i in result:
            self.content += f'\n{i}\n'
        return self.content


    def render(self, out_file):
        outtext = f'<{self.tag}>\n{self.content}\n</{self.tag}>'
        out_file.write(outtext)


e = Element('First Line', 'body')
e.append('Second Line\nThird line')

with open('test.html', 'w') as outf:
    e.render(outf)

# """
# Step 2 part A
# """
# html_sub = Element('HTML subclass 1st line', 'html')
# html_sub.append('')

