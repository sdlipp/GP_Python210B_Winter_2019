#!/usr/bin/env python3
import pytest

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = "html"
    def __init__(self, content=None,**kwargs):
        self.attributes = kwargs
        try:
            self.contents.append(content)
        except AttributeError:
            self.contents = []
            if content is not None:
                self.contents.append(content)


    def append(self, new_content):
        "appends content with new_content"
        self.contents.append(new_content)

    def render(self, out_file):
        self._open_tag(out_file)
        out_file.write('>\n')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        self._close_tag(out_file)

    def _open_tag(self,out_file):
        if self.attributes:
            out_file.write(f'<{self.tag} ')
            open_tag =[f'{key}="{value}" ' for key,value in self.attributes.items()]
            open_tag_string = ''.join(open_tag).rstrip()
            out_file.write(f'{open_tag_string}')
        else:
            out_file.write(f'<{self.tag}')

    def _close_tag(self,out_file):
        out_file.write(f'</{self.tag}>')




class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f'<{self.tag}>')
        out_file.write(self.contents[0])
        out_file.write(f'</{self.tag}>')

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    def render(self,out_file):
        Element._open_tag(self,out_file) #Can I use super here?
        out_file.write(f' />\n')


class Hr(SelfClosingTag):
    tag = "hr"
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Br(SelfClosingTag):
    tag = "br"
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
