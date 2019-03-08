#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
import functools


# This is the framework for the base class
class Element(object):
    indent = ''
    tag = 'html'

    def __init__(self, content=None, **attrs):
        self.attrs = attrs
        if content:
            self.content = [content]
        else:
            self.content = []

    def _front_tag(self):
        """Creates the front/opening tag"""
        return f'<{self.tag}>'

    def _end_tag(self):
        """Creates the ending tag"""
        return f'</{self.tag}>'

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_name, indent='', ind_count=0):
        # Writes the opening tag
        file_name.write(f'{self._front_tag()}\n')

        for content_line in self.content:
            if hasattr(content_line, 'render'):
                content_line.render(file_name, indent, ind_count + 1)
            else:
                file_name.write(f'{self.indent}{indent}{content_line}\n')
        file_name.write(f'{self._end_tag()}\n')


class Html(Element):
    """
    html sublcass
    """
    tag = 'html'

    def render(self, file_name, indent="", ind_count=0):
        self.indent = indent
        file_name.write(f'<!DOCTYPE html>\n')
        super().render(file_name, indent)


class P(Element):
    """
    class for p tag
    """
    tag = 'p'


class Body(Element):
    """
    class for p tag
    """
    tag = 'body'


"""
Step 3: print on one line
"""


class OneLineTag(Element):
    tag = 'Title'

    def render(self, file_name, indent="", ind_count=0):
        """
        Renders elements on a single line.
        :param file_name: Rendered object destination
        :param indent: Indentation level
        :param ind_count: Number of times indentation is to be applied
        """
        self.indent = indent * ind_count
        file_name.write(f'{self.indent}{self._front_tag()[:-1]} ')
        for k, v in self.attrs.items():
            file_name.write(f'{k}="{v}"')
        file_name.write(f'>')
        file_name.write(f'{self.content[0]}')
        file_name.write(f'{self._end_tag()}')

    def append(self, new_content):
        raise NotImplementedError


class Head(Element):
    tag = "head"


"""
Step 5: Self closing tag
"""


class SelfClosingTag(Element):
    tag = 'br'

    def append(self, new_content):
        raise NotImplementedError

    def render(self, file_name, indent="", ind_count=0):

        """
        if conent is entered this tells user that self closing tags
        can't have conent and resets the conent to an empty string.
        """

        self.indent = indent * ind_count

        if self.content:
            raise TypeError
        file_name.write(f'{self.indent}{self._front_tag()[:-1]}')
        for k, v in self.attrs.items():
            file_name.write(f'{k.rjust(len(k) + 1)}="{v}" />')


"""
Step 6
"""


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **attrs):
        if not (content and link):
            raise TypeError

        attrs['href'] = link
        super().__init__(content, **attrs)


class Ul(Element):
    """
    Step 7: Ul class
    """
    tag = 'ul'

    def __init__(self, content=None, **attrs):
        self.content = []
        self.attrs = attrs


class Li(Element):
    """
    Step 7: Li class
    """
    list_element = ''


class Meta(SelfClosingTag):
    """
    add meta tag
    """

    tag = 'meta'
