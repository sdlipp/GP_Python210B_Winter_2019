#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

        self.attributes = kwargs

    def _open_tag(self):
        return (f'<{self.tag}>')

    def _close_tag(self):
        return (f'</{self.tag}>')

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):

        out_file.write(self._open_tag()[:-1])
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(self._open_tag()[-1:] + '\n')

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content + '\n')
        out_file.write(self._close_tag() + '\n')


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


class OneLineTag(Element):

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file):
        out_file.write(self._open_tag()[:-1])
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(self._open_tag()[-1:])

        out_file.write(self.contents[0])
        out_file.write(self._close_tag() + '\n')


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError

        self.attributes = kwargs

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file):

        out_file.write(self._open_tag()[:-1])
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'
