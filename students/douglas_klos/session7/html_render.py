#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = 'html'

    def __init__(self, content=None):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write(f'<{self.tag}>\n')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f'</{self.tag}>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'