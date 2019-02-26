#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Element():
    '''
    The base rendering class
    '''
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        if content is None:
            content = ''
        self.contents = [content]

    def append(self, new_content):
        '''
        Appends strings as called
        '''
        self.contents.append(new_content)

    def render(self, out_file):
        '''
        Writes the outfile in question using data set and HTML tags
        '''
        open_tag = ["<{}".format(self.tag)]
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write("</{}>\n".format(self.tag))


class OneLineTag(Element):
    '''
    This is the class that processes HTML tags.  I think...
    '''
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    #pylint: disable=W0221
    def append(self, content):
        raise NotImplementedError


class Html(Element):
    '''
    Class definition for <html> tag
    '''
    tag = 'html'


class Body(Element):
    '''
    Class definition for <body> tag
    '''
    tag = 'body'

#pylint: disable=C0103
class P(Element):
    '''
    Class definition for <p> tag
    '''
    tag = 'p'


class Head(Element):
    '''
    Class definition for <head> tag
    '''
    tag = 'head'


class Title(OneLineTag):
    #pylint: disable=W0223
    '''
    Class definition for <title> tag
    '''
    tag = "title"
