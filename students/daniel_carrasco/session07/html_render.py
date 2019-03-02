#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        "initializes list, checks to see if any content is sent, if yes append"
        self.content = []
        self.htmlstart = "<html>\n"
        self.htmlend = "</html>"
        if content is not None:
            self.content.append(content)

    def append(self, new_content):
        "appends content with new_content"
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write(f'{self.htmlstart}')
        for line in self.content:
            out_file.write(line+'\n')
        out_file.write(f'{self.htmlend}')

page = Element("Some content")
page.append("Some more contenet")
with open("test.html", 'w') as outfile:
    page.render(outfile)