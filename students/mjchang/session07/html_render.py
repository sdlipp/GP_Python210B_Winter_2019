#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.contents = []
        if content:
            self.contents.append(content)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        for content in self.contents: #adding contents to file
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n") #newline to keep it readable
        out_file.write("</{}>\n".format(self.tag))

class OneLineTag(Element):
    def render(self, out_file,):
        for content in self.contents:
            out_file.write("<{}>".format(self.tag)) #removed newline
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content) #removed newline from Element
            out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = "title"
