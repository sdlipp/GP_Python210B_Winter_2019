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
            self.content += i
        return self.content


    # def render(self, out_file):
    #     outtext = f'<{self.tag}>\n{self.content}\n</{self.tag}>'
    #     out_file.write(outtext)

    def render2(self, file_name, open_method):
        outtext = f'<{self.tag}>\n{self.content}\n</{self.tag}>'
        with open(f'{file_name}.html', open_method) as file:
            file.write(outtext)


e = Element('First Line', 'body')
e.append('Second Line\nThird line')
e.render2('test', 'w')

"""
Step 2 part A
"""
html_sub = Element('HTML subclass 1st line', 'html')
html_sub.append('\nHTML subclass 2nd line')
html_sub.render2('html_subclass', 'w')

