#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content):
        if self.content:
            self.content += '\n' + new_content
        else:
            self.content = new_content

    def render(self, out_file):
        contentToHtml = f"<html>\n{self.content}\n</html>"
        out_file.write(contentToHtml)
        # out_file.write("just something as a place holder...")
