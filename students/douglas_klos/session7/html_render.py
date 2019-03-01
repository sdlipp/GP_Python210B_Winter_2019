#!/usr/bin/env python3
#pylint: disable=W0223,W0231,C0103,C0321

""" A class based system for rendering HTML """

# Douglas Klos
# March 1st, 2019
# Python 210, Session 7
# html_render.py


class Element():
    """
    Framework for a basic element in HTML code.

    Class attributes:
        tag:     Tag used for rendering html contents.  Base element class is set to html.
        indent:  The level of indentation for the current element.
    """
    tag = 'html'
    indent = ''

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for base Element class.

        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  Used for passing in tag attributes.

        Instance attributes:
            contents    The content that is to be rendered later into HTML format.
        """
        self.attributes = kwargs
        self.contents = [content] if content else []

    def _open_tag(self):
        """ Returns the opening tag for the current element """
        return f'<{self.tag}>'

    def _close_tag(self):
        """ Returns the closing tag for the current element """
        return f'</{self.tag}>'

    def append(self, new_content):
        """
        Appends new_content to the instance attribute content

        :param new_content: String that is to be appended to the instance content.
        """
        self.contents.append(new_content)

    def render(self, out_file, indent="", ind_count=0):
        """
        Recursively renders the instance attribute content into HTML format code.

        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied to the element.
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}\n')

        for content in self.contents:
            try:
                content.render(out_file, indent, ind_count + 1)
            except AttributeError:
                out_file.write(f'{self.indent}{indent}{content}\n')
        out_file.write(f'{self.indent}{self._close_tag()}\n')


class Html(Element):
    """
    Framework for 'html' tag.
    Inherits from Element.
    Overrides render method and tag class attribute.
    """
    tag = 'html'

    def render(self, out_file, indent="", ind_count=0):
        """
        Recursively renders the instance attribute content into HTML format code.

        Calls super().render after running

        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied to the element.
        """
        self.indent = indent
        out_file.write(f'<!DOCTYPE html>\n')
        super().render(out_file, indent)


class Body(Element):
    """
    Framework for 'body' tag.
    Inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'body'


class P(Element):
    """
    Framework for 'p' paragraph tag.
    Inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'p'


class Head(Element):
    """
    Framework for 'head' tag.
    Inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'head'


class Li(Element):
    """
    Framework for 'li' list item tag.
    Inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'li'


class Ul(Element):
    """
    Framework for 'ul' unordered list tag.
    Inherits from Element.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for Ul class.

        :param content: Accepts no content, raises TypeError if content is passed it.
        :param kwargs:  Used for passing in tag attributes.

        Attributes:
            contents    Ul class accepts no content and raises a TypeError if content is passed in.
        """
        if content: raise TypeError

        self.contents = []
        self.attributes = kwargs


class OneLineTag(Element):
    """
    Framework for elements that render on a single line, one line tags.
    Inherits from Element.
    Overrides append and render methods.
    """
    def append(self, new_content):
        """
        Overrides Element.append.
        One line tags can not append.
        Raises NotImplementedError if called.
        """
        raise NotImplementedError

    def render(self, out_file, indent="", ind_count=0):
        """
        Recursively renders the instance attribute content into HTML format code.

        Overrides Element.render

        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied for the element.
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}')
        out_file.write(f'{self.contents[0]}')
        out_file.write(f'{self._close_tag()}\n')


class H(OneLineTag):
    """
    Framework for 'h' header tag.
    Inherits from OneLineTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        """
        __init__ method for 'H' header class.

        Calls super().__init__ after execution

        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  Used for passing in tag attributes.
        """

        # Verifies function called with interger value for header level as first parameter.
        # If it was forgotten, then contents will likely be the first passed value.
        # This 'should' then fail if casted to an int, and raises a ValueError
        try:
            int(level)
        except ValueError:
            raise ValueError

        self.tag = f'h{level}'
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    """
    Framework for 'title' tag.
    Inherits from OneLineTag.
    Overrides tag class attribute.
    """
    tag = 'title'


class A(OneLineTag):
    """
    Framework for 'a' anchor tag.
    Inherits from OneLineTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        """
        __init__ method for 'a' anchor class.

        calls super().__init__ after execution

        :param link:    Anchor link passed in.  Added to kwargs and passed to super init.
        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  Used for passing in tag attributes.
        """
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    """
    Framework for self closing tag elements.
    Inherits from Element.
    Overrides __init__, append, and render methods.
    """
    def __init__(self, content=None, **kwargs):
        """
        __init__ method for SelfClosingTag class.

        :param content: Accepts no content, raises TypeError if content is passed it.
        :param kwargs:  Used for passing in tag attributes.
        """
        if content: raise TypeError

        self.attributes = kwargs

    def append(self, new_content):
        """
        Overrides Element.append.
        Self closing tags can not append.
        Raises NotImplementedError if called.
        """
        raise NotImplementedError

    def render(self, out_file, indent="", ind_count=0):
        """
        Recursively renders the instance attribute content into HTML format code

        :param out_file: destination for rendered text
        :param indent: the specified indentation level for elements
        :param ind_count: how many times indent should be applied for the element
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f' />\n')


class Hr(SelfClosingTag):
    """
    Framework for 'hr' horizontal rule tag.
    Inherits from SelfClosingTag.
    Overrides tag class attribute.
    """
    tag = 'hr'


# <br /> is XHTML format
class Br(SelfClosingTag):
    """
    Framework for 'br' horizontal rule tag.
    Inherits from SelfClosingTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'br'

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for Br class.

        Calls super().__init__ after running

        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  br elements accept no attributes.  Raises TypeError is passed in.
        """
        if kwargs: raise TypeError

        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    """
    Framework for 'meta' rule tag.
    Inherits from SelfClosingTag.
    Overrides tag class attribute.
    """
    tag = 'meta'
