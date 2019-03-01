#!/usr/bin/env python3

""" A class based system for rendering HTML """

# Douglas Klos
# February 27th, 2019
# Python 210, Session 7
# html_render.py


class Element():
    """ Framework for a basic element in HTML code """
    tag = 'html'
    indent = ''

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs

        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

    def _open_tag(self):
        return f'<{self.tag}>'

    def _close_tag(self):
        return f'</{self.tag}>'

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind="", ind_count=0):
        self.indent = cur_ind * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}\n')

        for content in self.contents:
            try:
                content.render(out_file, cur_ind, ind_count + 1)
            except AttributeError:
                out_file.write(f'{self.indent}{cur_ind}{content}\n')
        out_file.write(f'{self.indent}{self._close_tag()}\n')


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind="", ind_count=0):
        self.indent = cur_ind
        out_file.write(f'<!DOCTYPE html>\n')
        super().render(out_file, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Li(Element):
    tag = 'li'


class Ul(Element):
    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs

        if content is not None:
            raise TypeError
        else:
            self.contents = []


class OneLineTag(Element):

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file, cur_ind="", ind_count=0):
        self.indent = cur_ind * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}')
        out_file.write(f'{self.contents[0]}')
        out_file.write(f'{self._close_tag()}\n')


class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        try:
            int(level)
        except ValueError:
            raise ValueError

        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs

        if content is not None:
            raise TypeError

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file, cur_ind="", ind_count=0):
        self.indent = cur_ind * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


# <br /> is XHTML format
class Br(SelfClosingTag):
    tag = 'br'

    def __init__(self, content=None, **kwargs):
        if kwargs:
            raise TypeError

        super().__init__()


class Meta(SelfClosingTag):
    tag = 'meta'
