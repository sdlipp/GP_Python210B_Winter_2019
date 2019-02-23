#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    contents = ''
    tag = 'html'

    def __init__(self, content=None):
        # self.content += self.open_tag(self.tag)
        if content is not None:
            self.contents += content
        # self.content += self.close_tag(self.tag) + '\n'

    def append(self, new_content):
        try:
            self.contents += new_content
        except TypeError:
            self.contents += new_content.contents

    def open_tag(self, tag):
        return '<' + tag + '>'

    def close_tag(self, tag):
        return '</' + tag + '>'

    def render(self, out_file):
        out_file.write(self.open_tag(self.tag))
        out_file.write(self.contents)
        out_file.write('\n')
        out_file.write(self.close_tag(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'