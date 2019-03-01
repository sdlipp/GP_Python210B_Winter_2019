#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, contents=None, **kwargs):
        if contents:
            self.contents = [contents]
        else:
            self.contents = []

        self.kwargs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            for kwarg, value in self.kwargs.items():
                out_file.write(" {}='{}'".format(kwarg, value))
            out_file.write(">\n")
        else:
            out_file.write("<{}>\n".format(self.tag))

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write('\n')
        out_file.write("</{}>\n".format(self.tag))

        # contentToHtml = f"<{self.tag}>\n{' '.join(self.content)}\n</{self.tag}>"
        # out_file.write(contentToHtml)
        # out_file.write("just something as a place holder...")


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            for kwarg, value in self.kwargs.items():
                out_file.write(" {}='{}'".format(kwarg, value))
            out_file.write("> ")
        else:
            out_file.write("<{}> ".format(self.tag))

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(" </{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'
