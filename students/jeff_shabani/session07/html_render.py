#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None, tag=None, **attrs):
        self.attrs = attrs
        if tag:
            self.tag = tag
        else:
            self.tag = ''
        if content:
            self.content = content
        else:
            self.content = ''

    def append(self, new_content):
        result = list()
        result.append(new_content)
        for i in result:
            self.content += f'\n{i}\n'
        return self.content

    def render(self, file_name, open_method='w'):
        head = f'{self.tag.ljust(len(self.tag) + 1)}'
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{head}>\n{self.content}\n</{self.tag}>'
        with open(f'{file_name}.html', open_method) as file:
            file.write(outtext)


"""
Step 2 part B
"""


class HTML(Element):
    tag = 'html'


class PTag(Element):
    tag = 'p'


"""
Step 3: print on one line
"""


class OneLineTag(Element):

    def render(self, file_name, open_method='w'):
        self.tag = f'{self.tag}>'
        head = f'{self.tag.ljust(len(self.tag) + 1)}'
        for k, v in self.attrs.items():
            head += f'{k.rjust(len(k) + 1)}="{v}"'
        outtext = f'<{head}{self.content}</{self.tag}>'
        with open(f'{file_name}.html', open_method) as file:
            file.write(outtext)


"""
Step 5: Self closing tag
"""


class SelfClosingTag(Element):

    def render(self, file_name, open_method='w'):
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
        with open(f'{file_name}.html', open_method) as file:
            file.write(outtext)


if __name__ == '__main__':
    # e = Element("this is some text", 'body')
    # e.append("and this is some more text")
    # e.render('test')

    # html sub-class
    # html_sub = HTML('HTML subclass 1st line', 'html')
    # print(html_sub.tag)
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
    olt = OneLineTag('PythonClass - oneliner', 'title', style='text-align')
    olt.render('OneLingTagTest')
    #
    # """
    # step 4
    # """
    # attrs_test = Element('kwargs test', 'html',style='text-align', id='intro')
    # attrs_test.append('kwargstest line 2')
    # attrs_test.render('kwargs_test')

    """
    step 5 test for self closing tag
    """
    # sct_test = SelfClosingTag('html',style='text-align', id='intro')
    # sct_test = SelfClosingTag('_', 'html')
    # sct_test.render('sct_test')
    # print(dir(sct_test))
