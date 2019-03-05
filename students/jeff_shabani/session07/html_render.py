#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
import functools

# This is the framework for the base class
class Element(object):
    indent = ' ' * 2
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

    def render(self, file_name, cur_indent=''):
        # Writes the opening tag
        file_name.write(f'{self._front_tag()}\n')

        for content_line in self.content:
            if hasattr(content_line, 'render'):
                content_line.render(file_name)
            else:
                file_name.write(f'{content_line}\n')
        file_name.write(f'{self._end_tag()}\n')


class Html(Element):
    """
    html sublcass
    """
    tag = 'html'

    def render(self, file_name):
        file_name.write(f'<!DOCTYPE html>\n')
        super().render(file_name)


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

    Tag = 'Title'

    def render(self, file_name, cur_indent=''):
        """
        Renders elements on a single line.
        :param file_name:
        :param cur_indent:
        """
        file_name.write(f'{self._front_tag()} ')
        for k, v in self.attrs.items():
            file_name.write(f'{k}="{v}"')
        file_name.write(f'{self._front_tag()}')
        file_name.write(f'{self.content[0]}')
        file_name.write(f'{self._end_tag()}')

    def append(self, new_content):
        raise NotImplementedError




    # def render_alt(self, file_name):
    #     self.tag = f'{self.tag}>'
    #     head = f'{self.tag.ljust(len(self.tag) + 1)}'
    #     for k, v in self.kwargs.items():
    #         head += f'{k.rjust(len(k) + 1)}="{v}"'
    #     outtext = f'<{head}{self.content}</{self.tag}>'
    #     with open(f'{file_name}.html', 'w') as file:
    #         file.write(outtext)


"""
Step 5: Self closing tag
"""

# class SelfClosingTag(Element):
#
#     def render(self, file_name):
#
#         """
#         if conent is entered this tells user that self closing tags
#         can't have conent and resets the conent to an empty string.
#         """
#
#         if self.content:
#             print('Self closing tags cannot have content')
#         else:
#             self.content = ''
#
#         head = f'{self.tag.ljust(len(self.tag) + 1)}'
#         for k, v in self.kwargs.items():
#             head += f'{k.rjust(len(k) + 1)}="{v}"'
#         outtext = f'<{head}/>'
#         with open(f'{file_name}.html', 'w') as file:
#             file.write(outtext)

"""
Step 6
"""

# class A(Element):
#
#     def __init__(self, link, content):
#         self.link = link
#         self.content = content
#         super(Element).__init__()
#
#     def render(self, file_name):
#         head = 'a href='
#         tail = 'a'
#         outtext = f'<{head}"{self.link}">{self.content}</{tail}>'
#         with open(f'{file_name}.html', 'w') as file:
#             file.write(outtext)
#
# class Ul(Element):
#     """
#     Step 7: Ul class
#     """
#     ul = []
#
# class Li(Element):
#     """
#     Step 7: Li class
#     """
#     list_element = ''
#
# class Head(OneLineTag):
#
#     def __init__(self, level, content, tag=None, **kwargs):
#         self.level = level
#         self.content = content
#         self.tag = f'h{level}'
#         self.kwargs = kwargs
#         super(OneLineTag).__init__(list, tag, **kwargs)
#
# class Meta(SelfClosingTag):
#     """
#     add meta tag
#     """
#
#     def __init__(self, content=None, tag = 'meta charset="UTF-8"'):
#         super().__init__(content, tag)

# if __name__ == '__main__':
#
#     olt = OneLineTag('this is william')
#     olt.render(olt, 'tag')
