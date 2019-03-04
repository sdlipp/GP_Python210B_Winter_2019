#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    indent = ''
    tag = 'html'

    def __init__(self, content=None, tag=None, **attrs):
        self.attrs = attrs
        if tag:
            self.tag = tag
        else:
            self.tag = ''
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_name, cur_indent=''):
        if cur_indent:
            cur_indent = ' '*cur_indent
        head = f'{self.tag.ljust(len(self.tag) + 1)}'
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{cur_indent}{head}>\n{self.content}\n</{self.tag}>'
        with open(f'{file_name}.html', 'w') as file:
            file.write(outtext)


"""
Step 2 part B
"""


class HTML(Element):
    """
    html sublcass
    """
    tag = 'html'

    def render(self, file_name):
        head = f'!DOCTYPE {self.tag.ljust(len(self.tag) + 1)}'
        #super().render(file_name)
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{head}>\n{self.content}\n</{self.tag}>'
        with open(f'{file_name}.html', 'w') as file:
            file.write(outtext)


class PTag(Element):
    """
    class for p tag
    """
    tag = 'p'


"""
Step 3: print on one line
"""


class OneLineTag(Element):

    def render(self, file_name):
        self.tag = f'{self.tag}>'
        head = f'{self.tag.ljust(len(self.tag) + 1)}'
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{head}{self.content}</{self.tag}>'
        with open(f'{file_name}.html', 'w') as file:
            file.write(outtext)


"""
Step 5: Self closing tag
"""


class SelfClosingTag(Element):

    def render(self, file_name):

        """
        if conent is entered this tells user that self closing tags
        can't have conent and resets the conent to an empty string.
        """

        if self.content:
            print('Self closing tags cannot have content')
        else:
            self.content = ''

        head = f'{self.tag.ljust(len(self.tag) + 1)}'
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{head}/>'
        with open(f'{file_name}.html', 'w') as file:
            file.write(outtext)

"""
Step 6
"""

class A(Element):

    def __init__(self, link, content):
        self.link = link
        self.content = content
        super(Element).__init__()

    def render(self, file_name):
        head = 'a href='
        tail = 'a'
        outtext = f'<{head}"{self.link}">{self.content}</{tail}>'
        with open(f'{file_name}.html', 'w') as file:
            file.write(outtext)

class Ul(Element):
    """
    Step 7: Ul class
    """
    ul = []

class Li(Element):
    """
    Step 7: Li class
    """
    list_element = ''

class Header(OneLineTag):

    def __init__(self, level, content, tag=None, **attrs):
        self.level = level
        self.content = content
        self.tag = f'h{level}'
        self.attrs = attrs
        super(OneLineTag).__init__(list, tag, **attrs)

class Meta(SelfClosingTag):
    """
    add meta tag
    """

    def __init__(self, content=None, tag = 'meta charset="UTF-8"'):
        super().__init__(content, tag)


if __name__ == '__main__':
    # e = Element("this is some text", 'body')
    # e.append("and this is some more text")
    # e.render('test')

    #html sub-class
    # html_sub = HTML('HTML subclass 1st line', 'html')
    # html_sub.append('HTML subclass 2nd line')
    # html_sub.render('html_subclass')
    #
    # #p subclass
    # p_sub = PTag('p subclass 1st line', 'p')
    # p_sub.append('p subclass 2nd line')
    # p_sub.render('p_subclass')
    #
    """
    Step 3
    """

    # p = PTag('p')
    # p.render('ptag')
    # olt = OneLineTag('PythonClass - oneliner', 'title', style='text-align')
    # olt.render('OneLingTagTest')
    #
    # """
    # step 4
    # """
    # attrs_test = Element('kwargs test', 'html',style='text-align', id='intro')
    # attrs_test.append('kwargstest line 2')
    # attrs_test.render('kwargs_test')

    """
    step 5 self closing tag
    """
    # sct_test = SelfClosingTag('_','html')
    # sct_test.render('sct_test')
    # print(dir(sct_test))

    """
    step 6 A class
    """
    # A = A("http://google.com", "link to google")
    # A.render('google_test')

    """
    step 7
    """
    # h=Header(3, 'Dies ist Kopfebene')
    # h.render('header_test')
    #
    # meta_test = Meta()
    # meta_test.render('meta_test')
